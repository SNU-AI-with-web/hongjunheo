from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],   # ← OPTIONS 포함
    allow_headers=["*"],   # ← Content-Type 등 허용
)

class UserRequest(BaseModel):
    name: str
    age: int

class UserResponse(BaseModel):
    message: str
    is_adult: bool

@app.post("/user", response_model=UserResponse)
def check_user(data: UserRequest):
    return {
        "message": f"안녕 {data.name}!",
        "is_adult": data.age >= 20
    }