import streamlit as st

from utils.llm_helpers import summarize_with_gemini, summarize_with_openai, detect_language, sentiment_analysis
from utils.tokenizer_helpers import analyze_tokenization

st.title("Text Analysis Tool")
text=st.text_area("Enter your text here")

if st.button("Analyze"):
    if not text.strip():
        st.warning("Please enter some text first")
    else:
        st.header("Summaries")
        st.write("Gemini:\n",summarize_with_gemini(text))
        st.write("OpenAI:\n",summarize_with_openai(text))

        st.subheader("Tokenization Comparison")
        bert=analyze_tokenization("bert-base-uncased",text)
        gpt=analyze_tokenization("gpt2",text)
        st.write(f"BERT Tokens: {bert['token_count']}")
        st.write(f"GPT-2 Tokens: {gpt['token_count']}")

        st.subheader("Sentiment & Language")
        st.write("Detected Language:", detect_language(text))
        st.write("Sentiment:", sentiment_analysis(text))














# text = "Large Language Models are revolutionizing the way we interact with machines..."

# bert_tokens=analyze_tokenization("bert-base-uncased",text)
# gpt_tokens=analyze_tokenization("gpt2",text)

# print("BERT:", bert_tokens["token_count"], "tokens")
# print("GPT-2:", gpt_tokens["token_count"], "tokens")

# print("Gemini Summary:\n", summarize_with_gemini(text))
# print("\nOpenAI Summary:\n", summarize_with_openai(text))

# print("Detected Language:", detect_language(text))
# print("Sentiment:", sentiment_analysis(text))
