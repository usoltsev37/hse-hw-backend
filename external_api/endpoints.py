"""Module with endpoints for text-generation-summarization application"""
from fastapi import APIRouter
from pydantic import BaseModel
import requests

router = APIRouter()

ip = "127.0.0.1"
port_generate = "5048"
port_summarize = "5049"


class GetGenerateSummarizeRequest(BaseModel):
    prompt: str


@router.get("/generate_and_summarize/")
async def generate_and_summarize(request: GetGenerateSummarizeRequest):  # noqa: D103
    """
    Endpoint for text generation and summarization
    :param request: request.prompt beginning of sentence
    :return: json with status_code and result text
    """
    data_generate = {"prompt": request.prompt}
    response_generate = requests.get(f"http://{ip}:{port_generate}/generate", json=data_generate)

    print(response_generate.json())

    data_summarize = {"text": response_generate.json()["result"]}
    response_summarize = requests.get(f"http://{ip}:{port_summarize}/summarize", json=data_summarize)

    return {"status_code": 200, "result": response_summarize.json()["result"]}
