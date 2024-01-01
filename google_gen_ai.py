import google.generativeai as genai
import os 

GOOGLE_API_KEY='AIzaSyDQNjjw91ZFeG46uHiQDpyIfFE1RBaKCPU'

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-pro')

response = model.generate_content("What is the meaning of life?")

print(response.text)