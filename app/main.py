
from protocol import StreamPromptingSynapse

from pydantic import BaseModel
from typing import List

from fastapi import FastAPI
import uvicorn

from prompt import query_network


app = FastAPI()

class InputData(BaseModel):
    roles: List[str]=["system", "user"]
    messages: List[str]=["Write an essay of 100 words on World War 1", "Write an essay of 100 words on World War 1"]


@app.post("/text-to-text", responses={200:{"description":"text to text"}})
async def text_to_text(input_data: InputData):

    messages=input_data.messages
    roles=input_data.roles

    synapse = StreamPromptingSynapse(
    roles=roles,
    messages=messages,
    completion="",  # will be filled after processing
    required_hash_fields=["messages"],
    timeout=500.0,  # timeout in seconds
    )

    return await query_network(synapse)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)

