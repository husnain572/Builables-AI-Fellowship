import os 
from dotenv import load_dotenv
from openai import OpenAI
import google.generativeai as genai
from textblob import TextBlob
from langid import classify


load_dotenv()

GEMINI_API_KEY=os.getenv("GEMINI_API_KEY")
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")

# Setup clients
genai.configure(api_key=GEMINI_API_KEY)
openai_client=OpenAI(api_key=OPENAI_API_KEY)

def summarize_with_gemini(text):
    try:
        model = genai.GenerativeModel("gemini-2.5-pro")
        response = model.generate_content(f"Summarize this text in 2 lines:\n{text}")
        
        # Try different ways to get the text safely
        if hasattr(response, "text") and response.text:
            return response.text.strip()
        elif response.candidates:
            return response.candidates[0].content.parts[0].text.strip()
        else:
            return "No summary generated."
    except Exception as e:
        return f"Error with Gemini: {e}"
    
def summarize_with_openai(text):
    try:
        response=openai_client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role":"user", "content":f"Summarize this text:\n{text}"}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error with OpenAI: {e}"


def detect_language(text):
    lang, _ = classify(text)
    return lang


def sentiment_analysis(text):
    blob=TextBlob(text)
    polarity=blob.sentiment.polarity
    sentiment="Positive" if polarity >0 else "Negative" if polarity<0 else "Neutral"
    return sentiment