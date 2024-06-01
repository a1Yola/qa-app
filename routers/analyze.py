from fastapi import APIRouter, Form, Request, Response
from fastapi.encoders import jsonable_encoder
import json

from utils.get_csv import get_csv

router = APIRouter()

@router.post("/analyze")
async def chat(request: Request, pdf_filename: str = Form(...)):
    output_file = get_csv(pdf_filename)
    response_data = jsonable_encoder(json.dumps({"output_file": output_file}))
    res = Response(response_data)
    return res
