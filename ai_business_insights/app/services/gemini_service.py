import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini API
genai.configure(api_key=API_KEY)

def generate_gemini_response(prompt):
    """
    Send a prompt to Google Gemini API and return the response.
    """
    try:
        model = genai.GenerativeModel("gemini-2.0-flash")
        
        response = model.generate_content(prompt)

        if response and response.text:
            return response.text
        else:
            return "No valid response received."
    
    except Exception as e:
        print(f"Error with Gemini API: {e}")
        return "Error: Unable to fetch response from Gemini API."

def generate_multi_step_response(prompts):
    """
    Chain multiple prompts to create a multi-step response.
    """
    combined_response = []

    for prompt in prompts:
        response = generate_gemini_response(prompt)
        combined_response.append(response)

    return "\n\n".join(combined_response)
