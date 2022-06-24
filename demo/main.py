from fastapi import FastAPI
import transformers

app = FastAPI()

from transformers import BertTokenizer
tokenizer = BertTokenizer(vocab_file="/data/wang/models/bmm/vocab/bpe_cn/vocab.txt")




@app.get("/{sentence}")
async def root(sentence):

    tokens = tokenizer.tokenize(sentence)
    token_id = tokenizer.convert_tokens_to_ids(tokens)
    id2token = tokenizer.convert_ids_to_tokens(token_id)

    return {"tokens": tokens,
            "token_id":token_id,
            "id2token":id2token,
            'code': '200'
            }
