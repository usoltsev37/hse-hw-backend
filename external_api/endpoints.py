"""Module with endpoints for text-generation-summarization application"""
from fastapi import APIRouter
from pydantic import BaseModel
import requests

router = APIRouter()

IP = "127.0.0.1"
PORT_GENERATE = "5048"
PORT_SUMMARIZE = "5049"


class GetGenerateSummarizeRequest(BaseModel):
    """ Request for our service """
    prompt: str


@router.get("/generate_and_summarize/")
async def generate_and_summarize(request: GetGenerateSummarizeRequest):  # noqa: D103
    """
    Endpoint for text generation and summarization
    :param request: request.prompt beginning of sentence
    :return: json with status_code and result text
    """
    data_generate = {"prompt": request.prompt}
    response_generate = requests.get(f"http://{IP}:{PORT_GENERATE}/generate", json=data_generate)

    print(response_generate.json())

    data_summarize = {"text": response_generate.json()["result"]}
    response_summarize = requests.get(
        f"http://{IP}:{PORT_SUMMARIZE}/summarize",
        json=data_summarize
    )

    return {"status_code": 200, "result": response_summarize.json()["result"]}
