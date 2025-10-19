from utils.tokenizer_helpers import analyze_tokenization

def test_tokenizer():
    result = analyze_tokenization("bert-base-uncased", "Hello world")
    assert "token_count" in result
