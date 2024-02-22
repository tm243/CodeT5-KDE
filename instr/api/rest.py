"""
Basic REST API
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel

from transformers import AutoModelForSeq2SeqLM
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("Salesforce/codet5p-770m")
model = AutoModelForSeq2SeqLM.from_pretrained('api/trained/kde-cpp-qml-instructions/final_checkpoint/')
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

class InstructionItem(BaseModel):
    instr: str

@app.get('/')
def index():
    return {
        "info": ["CodeT5+ KDE-C++ Instructions"]
    }

@app.post("/generate")
def generate(request: InstructionItem):
    instr = request.instr

    input_ids = tokenizer(instr, return_tensors='pt').input_ids
    outputs = model.generate(input_ids, max_new_tokens=300)
    code = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return {
        "code" : code
        }
