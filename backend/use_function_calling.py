import json
import os
from openai import OpenAI
from dotenv import load_dotenv
import requests
import base64

load_dotenv()

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
model = "gpt-4o"

tools = [
    {
        "type": "function",
        "name": "get_current_weather",
        "description": "Get current weather.",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {
                    "type": "string",
                    "description": "City name, e.g., Seoul, New York",
                },
            },
            "required": ["city"],
        },
    },
]

def basic_response(user_input):
    input_list = [{"role": "user", "content": user_input}]

    response = client.responses.create(
        model=model,
        instructions="당신은 유능한 조수입니다.",
        input=input_list,
        tools=tools,
    )

    output = response.output_text

    print(f"[debug-server] response: {response}")

    if response.output[0].type == "function_call":
        function_name = response.output[0].name
        arguments = response.output[0].arguments

        if function_name == "get_current_weather":
            city = json.loads(arguments).get("city")
            weather_info = get_current_weather(city)
            function_call_response = client.responses.create(
                model=model,
                instructions="당신은 유능한 조수입니다.",
                input=input_list + response.output + [
                    {
                        "type": "function_call_output",
                        "call_id": response.output[0].call_id,
                        "output": weather_info
                    }
                ],
                tools=tools,
            )
            output = function_call_response.output_text

    return output

def get_current_weather(city: str) -> str:
    print(f"[debug-server] get_current_weather({city})")

    endpoint = "https://wttr.in"
    try:
        response = requests.get(f"{endpoint}/{city}")
        print(f"[debug-server] Weather API response status: {response.status_code}")
        print(f"[debug-server] Weather API response text: {response.text}")
        
        if response.status_code == 200:
            return response.text
        elif response.status_code == 403:
            print("[ERROR] Weather API access forbidden")
            return "날씨 정보를 가져오는데 권한이 없습니다. API 접근이 거부되었습니다."
        elif response.status_code == 404:
            print("[ERROR] City not found")
            return f"'{city}'의 날씨 정보를 찾을 수 없습니다."
        elif response.status_code == 429:
            print("[ERROR] Too many requests")
            return "날씨 정보 요청이 너무 많습니다. 잠시 후 다시 시도해주세요."
        else:
            print(f"[ERROR] Weather API error: {response.status_code}")
            return f"날씨 정보를 가져오는데 실패했습니다. (상태 코드: {response.status_code})"
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Weather API request failed: {str(e)}")
        return f"날씨 정보를 가져오는데 실패했습니다: {str(e)}"

if __name__ == "__main__":
    print("=== Basic Response ===")
    result = basic_response("서울 날씨 알려줘")
    print(result)

