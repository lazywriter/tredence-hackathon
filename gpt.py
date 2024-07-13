import os
import google.generativeai as genai 
from dotenv import load_dotenv
load_dotenv()
genai.configure(
    api_key="AIzaSyAeag4eROMoZYEpVrFBmiQNXLWyJucatL4"
)
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])
question = input("You: ")

response = chat.send_message(question)
print('\n')
print(f"Bot: {response.text}") 
print('\n')