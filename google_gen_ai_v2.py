# pip3.11 install google-generativeai==0.3.1
import google.generativeai as genai2

# Need to use a new API key in 
genai2.configure(api_key="AIzaSyD10xVFJ0vpPJxS1RBg44OXQWZpK9GG_6M")

model = genai2.GenerativeModel('gemini-pro')

prompt = 'Okay I dont need coffees and um five water bottles and five more water glasses. lets see. mmmmmm three cups of tea.'
command = 'Give the count of coffee, water and tea as a JSON object.'

response = model.generate_content(prompt + command)

print(response.text)