from fastapi import FastAPI
import transformers
from transformers import pipeline
app = FastAPI()

unmasker = pipeline('fill-mask', model='bert-base-uncased')

#
@app.get("/{sentence}")
async def root(sentence):
    output=unmasker("Hello I'm a [MASK] model.")
    return {"output": output,
            'code': '200'
            }
