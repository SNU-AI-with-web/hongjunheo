import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
model = "gpt-5"

data_store = {
    "철수": "20",
    "영희": "16",
}

def basic_response(user_input):
    response = client.responses.create(
        model=model,
        instructions="당신은 유능한 조수입니다.",
        input=user_input,
    )
    return response.output_text

if __name__ == "__main__":
    user_input = "영희는 성인인가요?"
    print("=== Basic Response without RAG ===")
    result = basic_response(user_input)
    print(result)

    name = user_input[:2]

    rag_data = f"{name}의 나이는 {data_store[name]}살 입니다."

    print("=== Basic Response with RAG ===")
    result = basic_response(rag_data + " " + user_input)
    print(result)


