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

def review_code(code):
    try:
        # Generate content using model.generate_content
        response = model.generate_content(code)  # Passing code directly to the model
        fixed_code = response.text  # Adjust based on the response structure

        # If issues are part of the response, you can extract them
        issues = response.issues if hasattr(response, 'issues') else []
        
        return fixed_code, issues  # Return both fixed code and issues
    except Exception as e:
        return None, [f"Error generating content: {e}"]

def main():
    st.title("AI Code Reviewer")
    
    # Input section for Python code
    code = st.text_area("Enter your Python code here")

    if st.button("Review Code"):
        if code:
            try:
                # Get the response from the AI model
                fixed_code, issues = review_code(code)
                
                # Display the Bug Report if there are issues
                if issues:
                    st.markdown("### Bug Report")
                    for issue in issues:
                        st.markdown(f"- {issue}")
                else:
                    st.markdown("### Bug Report")
                    st.markdown("No issues were found in your code.")

                # Display the fixed code under a separate section
                if fixed_code:
                    st.markdown("### Fixed Code")
                    st.code(fixed_code, language='python')
                    
            except Exception as e:
                st.error(f"Error reviewing code: {e}")
        else:
            st.warning("Please enter your code.")

if __name__ == "__main__":
    main()
