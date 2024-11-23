import os
from dotenv import load_dotenv
import streamlit as st
from PIL import Image
import pytesseract
from gtts import gTTS
import google.generativeai as genai
import tempfile

# Load environment variables
load_dotenv()

# Load Gemini API Key from .env file
GEMINI_API_KEY = os.getenv("GOOGLE_GENERATIVE_AI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("GOOGLE_GENERATIVE_AI_API_KEY is not set. Add it to the .env file.")

# Initialize Google Generative AI with the API key
genai.configure(api_key=GEMINI_API_KEY)

# Streamlit app setup
st.set_page_config(page_title="AI-Assist", layout="wide")

# CSS for Netflix-style intro
def add_intro_animation():
    st.markdown(
        """
        <style>
        .intro-container {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: black;
            display: flex;
            justify-content: center;
            align-items: center;
            z-index: 9999;
            animation: fadeOut 3s ease-out 3s forwards;
        }

        .intro-title {
            font-size: 4rem;
            color: white;
            font-family: 'Arial', sans-serif;
            text-align: center;
            animation: zoomIn 1.5s ease-out;
        }

        @keyframes zoomIn {
            0% {
                transform: scale(0.3);
                opacity: 0;
            }
            100% {
                transform: scale(1);
                opacity: 1;
            }
        }

        @keyframes fadeOut {
            0% {
                opacity: 1;
            }
            100% {
                opacity: 0;
                visibility: hidden;
            }
        }
        </style>
        <div class="intro-container">
            <div class="intro-title">👓 Visionary AI</div>
        </div>
        """,
        unsafe_allow_html=True
    )


# Function to generate scene description using Gemini API
def generate_scene_description(input_prompt, image_data):
    try:
        model = genai.GenerativeModel('gemini-1.5-pro')
        response = model.generate_content([input_prompt, image_data[0]])
        return response.text
    except Exception as e:
        return f"Error generating scene description: {e}"


# Function to extract text from the image using Tesseract OCR
def extract_text_from_image(image):
    try:
        return pytesseract.image_to_string(image)
    except Exception as e:
        return f"Error extracting text: {e}"


# Function to convert text to speech using gTTS and save to a file
def text_to_speech(text):
    try:
        tts = gTTS(text)
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio_file:
            audio_path = temp_audio_file.name
            tts.save(audio_path)
            return audio_path
    except Exception as e:
        st.error(f"Error during text-to-speech conversion: {e}")
        return None


# Main app logic
def main():
    # Display intro animation
    add_intro_animation()

    # Main Overview Section
    st.title("🔍✨ Navigating the World Through AI Vision")

    # Unified Image Upload
    st.header("Upload an Image for Processing")
    uploaded_file = st.file_uploader("📤 Upload an image for all features...", type=["jpg", "jpeg", "png"])

    if uploaded_file:
        # Display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", width=400)

        # Convert image to bytes for API and reuse
        image_bytes = uploaded_file.getvalue()
        image_parts = [{"mime_type": "image/jpeg", "data": image_bytes}]

        # Feature Options
        st.header("Select a Feature to Process")
        col1, col2, col3 = st.columns(3)

        # Feature 1: Describe Image
        with col1:
            if st.button("📜 Describe Image"):
                input_prompt = """
                You are an AI assistant helping visually impaired individuals by describing the scene in the image. Provide:
                1. List of items detected in the image with their purpose.
                2. Overall description of the image.
                3. Suggestions for actions or precautions for the visually impaired.
                """
                with st.spinner("Generating scene description..."):
                    description = generate_scene_description(input_prompt, image_parts)
                    st.subheader("Scene Description")
                    st.write(description)

        # Feature 2: Extract Text
        with col2:
            if st.button("📝 Extract Text"):
                with st.spinner("Extracting text from image..."):
                    text = extract_text_from_image(image)
                    st.subheader("Extracted Text")
                    st.write(text)

        # Feature 3: Play & Download Speech
        with col3:
            if st.button("🔊 Play & Download Speech"):
                with st.spinner("Converting text to speech..."):
                    text = extract_text_from_image(image)
                    if text.strip():
                        audio_path = text_to_speech(text)
                        if audio_path:
                            st.success("Text-to-Speech Conversion Completed!")
                            st.audio(audio_path, format="audio/mp3", start_time=0)
                            st.download_button(
                                label="Download Audio",
                                data=open(audio_path, "rb"),
                                file_name="speech_output.mp3",
                                mime="audio/mp3"
                            )
                            os.remove(audio_path)
                    else:
                        st.warning("No text found in the image.")


if __name__ == "__main__":
    main()
