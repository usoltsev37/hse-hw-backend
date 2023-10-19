"""Module with endpoints for text-summarization application"""
from fastapi import APIRouter
from pydantic import BaseModel
from transformers import pipeline, set_seed

router = APIRouter()

set_seed(0)
MIN_LENGTH = 10
MAX_LENGTH = 50

summarization = pipeline("summarization", model='facebook/bart-large-cnn', min_length=MIN_LENGTH, max_length=MAX_LENGTH)


class GetSummarizeRequest(BaseModel):
    text: str


@router.get("/summarize/")
async def summarize(request: GetSummarizeRequest):  # noqa: D103
    """
    Endpoint for text summarization
    :param request: request.text for summarization
    :return: json with status_code and result text
    """
    result = summarization(request.text)
    return {"status_code": 200, "result": result}
