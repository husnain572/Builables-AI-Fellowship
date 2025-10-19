# Usage Examples

## Example 1: Analyze Text
```python
from main import analyze_text

text = "Artificial Intelligence is transforming the world."
results = analyze_text(text)
print(results)


from utils.tokenizer_helpers import analyze_tokenization

tokens = analyze_tokenization("bert-base-uncased", "Machine learning is fun!")
print(tokens)


from main import analyze_sentiment

sentiment = analyze_sentiment("I love using AI tools!")
print(sentiment)
