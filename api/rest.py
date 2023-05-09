"""
Basic REST API
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel

from transformers import T5ForConditionalGeneration
from transformers import RobertaTokenizer

tokenizer = RobertaTokenizer.from_pretrained("Salesforce/codet5-small")
model = T5ForConditionalGeneration.from_pretrained('api/saved-pretrained-kde-cpp-tm')
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Item(BaseModel):
    name: str

class SummaryItem(BaseModel):
    code: str

@app.get('/')
def index():
    return {
        "info": ["CodeT5 KDE-C++ Summary"]
    }

@app.post("/summary")
def single_essay_scoring(request: SummaryItem):
    code = request.code

    input_ids = tokenizer(code, return_tensors='pt').input_ids
    outputs = model.generate(input_ids)
    summary = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return {
        "summary" : summary
        }
