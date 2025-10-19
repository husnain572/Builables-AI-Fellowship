from transformers import AutoTokenizer

def analyze_tokenization(model_name,text):
    tokenizer=AutoTokenizer.from_pretrained(model_name)
    tokens=tokenizer.tokenize(text)
    token_count=len(tokens)
    return{
        "model":model_name,
        "tokens": tokens,
        "token_count":token_count
    }

