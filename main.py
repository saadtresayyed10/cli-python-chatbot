import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
genai.configure(api_key=API_KEY)

def chatWithGemini(prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    
    if response and hasattr(response, "text"):
        return response.text.strip()
    return "I cannot understand this..."


if __name__ == "__main__":
    while True:
        userInput = input("You: ")
        if userInput in ["exit", "quit", "bye", "goodbye", "see ya later", "peace", "adios"]:
            print("Goodbye!")
            break
        response = chatWithGemini(userInput)
        print(f"Bot: {response}")