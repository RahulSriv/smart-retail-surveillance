import google.generativeai as genai
import os
from dotenv import load_dotenv
from PIL import Image

# Load key from .env
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Load image
img = Image.open("resources/input/sample.jpg")

# Use Gemini Vision
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content(["What is happening in this image?", img])

print(response.text)
