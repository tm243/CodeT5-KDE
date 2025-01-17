"""
Inference example
"""

from transformers import T5ForConditionalGeneration
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("Salesforce/codet5p-770m")
model = AutoModelForSeq2SeqLM.from_pretrained('api/trained/kde-cpp-qml-instructions/final_checkpoint/')

instr = """
Write a function to find the maximum difference between two numbers in a given array.
"""

input_ids = tokenizer(instr, return_tensors='pt').input_ids
outputs = model.generate(input_ids, max_new_tokens=300)

print("Result:", tokenizer.decode(outputs[0], skip_special_tokens=True))

