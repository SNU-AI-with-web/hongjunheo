import os
from openai import OpenAI
from dotenv import load_dotenv
import base64

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

def image_response(user_input):
    response = client.responses.create(
        model=model,
        input=user_input,
        tools=[{"type": "image_generation"}]
    )
    # Save the image to a file
    image_data = [
        output.result
        for output in response.output
        if output.type == "image_generation_call"
    ]
        
    if image_data:
        image_base64 = image_data[0]
        with open("output_image.png", "wb") as f:
            f.write(base64.b64decode(image_base64))

def stream_response(user_input):
    stream = client.responses.create(
        model=model,
        input=user_input,
        stream=True,
    )
    for event in stream:
        print(event)

if __name__ == "__main__":
    # print("=== Basic Response ===")
    # result = basic_response("한국의 수도는 어디야?")
    # print(result)

    print("\n=== Image Response ===")
    image_response("귀여운 강아지 그림 그려줘.")

    # print("\n=== Stream Response (Events) ===")
    # stream_response("간단한 코딩 농담 알려줘.")

