import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
genai.configure(api_key=API_KEY)

def chatWithGemini(prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    return response.text

while True:
    userInput = input("You: ")
    if userInput in ["exit", "quit"]:
        print("Goodbye!")
        break
    response = chatWithGemini(userInput)
    print(f"Bot: {response}")