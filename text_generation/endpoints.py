"""Module with endpoints for text-generation application"""
from fastapi import APIRouter
from pydantic import BaseModel
from transformers import pipeline, set_seed

router = APIRouter()
generator = pipeline('text-generation', model='distilgpt2')

set_seed(0)
MAX_LENGTH = 200


class GetGenerateRequest(BaseModel):
    prompt: str


@router.get("/generate/")
async def generate(request: GetGenerateRequest):  # noqa: D103
    """
    Endpoint for text generation which starts with prompt
    :param request: request.prompt beginning of sentence
    :return: json with status_code and result text
    """
    result = generator(
        request.prompt,
        max_length=MAX_LENGTH,
        num_return_sequences=1
    )[0]['generated_text'].replace('\n', ' ')
    return {"status_code": 200, "result": result}
