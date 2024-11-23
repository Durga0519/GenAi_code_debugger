import streamlit as st

# Custom CSS for the intro animation and modal
custom_css = """
<style>
/* Full-screen Intro Animation */
#intro {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: black;
    color: white;
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 9999;
    animation: fadeOut 5s ease-in-out forwards;
}

/* Logo animation */
#logo {
    font-size: 3em;
    font-weight: bold;
    animation: zoomIn 1.5s ease-in-out;
}

/* Zoom-in effect */
@keyframes zoomIn {
    0% { transform: scale(0.5); opacity: 0; }
    100% { transform: scale(1); opacity: 1; }
}

/* Fade-out effect */
@keyframes fadeOut {
    0% { opacity: 1; }
    100% { opacity: 0; display: none; }
}

/* Modal Pop-Up */
.modal {
    display: none;
    position: fixed;
    z-index: 9998;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    overflow: auto;
    background-color: rgba(0, 0, 0, 0.8);
}

.modal-content {
    background-color: white;
    margin: 15% auto;
    padding: 20px;
    border-radius: 10px;
    width: 50%;
    text-align: center;
}

.modal-button {
    background-color: #4CAF50;
    color: white;
    padding: 10px 20px;
    margin: 10px;
    border: none;
    cursor: pointer;
    border-radius: 5px;
}

.modal-button:hover {
    background-color: #45a049;
}
</style>

<div id="intro">
    <div id="logo">Netflix-like Intro</div>
</div>

<!-- Modal -->
<div id="myModal" class="modal">
    <div class="modal-content">
        <h2>Select a Feature</h2>
        <button class="modal-button" onclick="document.getElementById('describe-image').click()">Describe Image</button>
        <button class="modal-button" onclick="document.getElementById('extract-text').click()">Extract Text</button>
        <button class="modal-button" onclick="document.getElementById('text-to-speech').click()">Text-to-Speech</button>
    </div>
</div>

<script>
document.addEventListener('DOMContentLoaded', (event) => {
    setTimeout(() => {
        document.getElementById('myModal').style.display = 'block';
    }, 3000); // Show modal after intro animation
});
</script>
"""

# Display the custom CSS and HTML
st.markdown(custom_css, unsafe_allow_html=True)

# Buttons for the features
if st.button("Describe Image", key="describe-image"):
    uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
    if uploaded_file:
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
        st.write("Here, you'd implement the image description feature.")

if st.button("Extract Text", key="extract-text"):
    uploaded_file = st.file_uploader("Upload an image or document for text extraction", type=["png", "jpg", "jpeg", "pdf"])
    if uploaded_file:
        st.write("Here, you'd implement the text extraction feature.")

if st.button("Text-to-Speech", key="text-to-speech"):
    text_input = st.text_area("Enter text to convert to speech")
    if st.button("Convert"):
        st.write("Here, you'd implement the text-to-speech feature.")

# Hide Streamlit's default elements during the intro
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
