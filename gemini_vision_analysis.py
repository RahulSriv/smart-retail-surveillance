import os
import google.generativeai as genai
from PIL import Image
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Load an image you want Gemini to analyze
image_path = "resources/output/extracted_frames/frame_0004.jpg"
image = Image.open(image_path)

# Create the multimodal model
model = genai.GenerativeModel("gemini-1.5-flash")

# Ask a behavior-related question
prompt = "Describe what is happening in this retail surveillance frame. Is there any suspicious or shoplifting behavior?"

response = model.generate_content([prompt, image])

print("\n--- GEMINI'S ANALYSIS ---")
print(response.text)
