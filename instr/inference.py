"""
Inference example
"""

from transformers import T5ForConditionalGeneration
from transformers import RobertaTokenizer

tokenizer = AutoTokenizer.from_pretrained("Salesforce/codet5p-770m")
model = AutoModelForSeq2SeqLM.from_pretrained('api/saved-pretrained-kde-cpp-tm')

instr = """
Write a function to find the maximum difference between two numbers in a given array.
"""

input_ids = tokenizer(instr, return_tensors='pt').input_ids
outputs = model.generate(input_ids, max_new_tokens=300)

print("Result:", tokenizer.decode(outputs[0], skip_special_tokens=True))

