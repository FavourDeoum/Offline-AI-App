from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Request(BaseModel):
    user_input: str

@app.post("/api/recommend")
def recommend(data: Request):
    response = generate_response(data.user_input)
    return {"recommendation": response}
