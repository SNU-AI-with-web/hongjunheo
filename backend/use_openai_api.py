import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
model = "gpt-5"

def basic_response(user_input):
    response = client.responses.create(
        model=model,
        instructions="당신은 유능한 조수입니다.",
        input=user_input,
    )
    return response.output_text

def simple_response(user_input):
    response = client.responses.create(
        model=model,
        input=user_input,
    )
    return response.output_text

def stream_response(user_input):
    stream = client.responses.create(
        model=model,
        input=user_input,
        stream=True,
    )
    for event in stream:
        print(event)

if __name__ == "__main__":
    print("=== Basic Response ===")
    result = basic_response("한국의 수도는 어디야?")
    print(result)

    print("\n=== Simple Response ===")
    result = simple_response("재미있는 농담 하나 해줘.")
    print(result)

    print("\n=== Stream Response (Events) ===")
    stream_response("간단한 코딩 농담 알려줘.")

