from fastapi import FastAPI
import transformers

app = FastAPI()

from transformers import BertTokenizer
tokenizer = BertTokenizer(vocab_file="/data/wang/models/bmm/vocab/bpe_cn/vocab.txt")




@app.get("/")
async def root():
    examples = ["我爱北京天安门", "天安门广场吃炸鸡"]

    tokens = tokenizer.tokenize(examples[0])

    token_id = tokenizer.convert_tokens_to_ids(tokens)

    id2token = tokenizer.convert_ids_to_tokens(token_id)

    return {"tokens": tokens,
            "token_id":token_id,
            "id2token":id2token,
            'code': '200'
            }
