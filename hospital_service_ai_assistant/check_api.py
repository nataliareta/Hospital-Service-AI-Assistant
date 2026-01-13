import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    print("GOOGLE_API_KEY not found")
    exit()

try:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-2.0-flash-lite")
    response = model.generate_content("Hello")

    print("API GEMINI ACTIVE")
    print("Response:", response.text)

except Exception as e:
    print("API GEMINI ERROR")
    print(e)
    
    import os
    print("API KEY USED:", os.getenv("GOOGLE_API_KEY")[:8])