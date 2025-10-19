from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

api_key=os.getenv("OPENAI_API_KEY")
client=OpenAI(api_key=api_key)  

system_prompt={
    "professional":"You are a professinal assistant. Responsd in a formal business-like tone.",
    "creative":"You are a creative companion who loves imagination and storytelling.",
    "technical":"You are technical expert who gives detailes and precise explanation."
}

print("Choose mode: Professional / Creative / Technical")
mode=input("Mode: ").lower()
system_prompt=system_prompt.get(mode, system_prompt["professional"])

def chat():
    print("Simple chatBot (type 'exit' or quit)\n")
    messages=[{
        "role":"system", "content":system_prompt 
    }]
    while True:
        user_input=input("You: ")
        if user_input.lower() in ["quit", "exit"]:
            break

        messages.append({"role":"user", "content":user_input})
        try:
            response=client.chat.completions.create(
                model="gpt-4o-mini",
                messages=messages
            )
            reply=response.choices[0].message.content
            print("Assistant: ", reply)
            messages.append({"role":"assistant","content":reply})
        except Exception as e:
            print("Error:",e)


if __name__=="__main__":
    chat()