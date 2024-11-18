import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure API key for Google Generative AI
api_key = os.getenv("API_KEY")
genai.configure(api_key=api_key)

# Instantiate the model
model = genai.GenerativeModel("gemini-1.5-flash")

# System prompt for bug detection
sys_prompt = """
You are an expert AI code reviewer integrated into a user-friendly Python application. Your role is to analyze Python code submitted by users and provide the following:
1. ## Bug Report: Identify potential bugs, syntax errors, and logical flaws in the code.
2. ## Fixed Code: Return fixed or optimized code snippets alongside explanations of the changes made.
Maintain a professional tone and focus solely on identifying and fixing issues. Avoid additional guidance or commentary.
"""

def generate_bug_report_and_fixed_code(code):
    """Use the AI model to generate the bug report and fixed code."""
    try:
        response = model.generate_content([sys_prompt, code])
        # Return the full response text containing Bug Report and Fixed Code
        return response.text if hasattr(response, 'text') else "No response generated."
    except Exception as e:
        return f"Error generating content: {e}"

def main():
    st.title("GenAI Code Reviewer")
    
    # Input section for Python code
    code = st.text_area("Enter your Python code here", height=200, max_chars=10000)

    if st.button("Review Code"):
        if code:
            try:
                # Get the Bug Report and Fixed Code using the system prompt
                response = generate_bug_report_and_fixed_code(code)

                # Display the Bug Report and Fixed Code
                st.markdown(response)

            except Exception as e:
                st.error(f"Error reviewing code: {e}")
        else:
            st.warning("Please enter your code.")

if __name__ == "__main__":
    main()
