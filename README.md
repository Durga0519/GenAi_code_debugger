# GenAi_code_debugger
## Overview
The AI Code Reviewer is a Python-based web application designed to assist developers by reviewing Python code, identifying bugs, and providing corrected versions of the code. Built using Streamlit and powered by Google Generative AI, this tool offers a seamless and user-friendly interface for improving code quality.

## Features
- **Bug Detection**: Highlights potential bugs, syntax errors, and logical flaws in the submitted Python code.
- **Code Correction**: Provides a fixed or optimized version of the submitted code.
- **Streamlined Interface**: Clean and simple design with expanded input areas for ease of use.
- **Powered by AI**: Leverages advanced generative AI models for precise and efficient code reviews.

## How It Works
1. Users input their Python code in the provided text area.
2. The AI model analyzes the code for issues and generates:
   - A **Bug Report** detailing identified problems.
   - A **Fixed Code** section with corrections or optimizations.
3. Results are displayed in a professional and easy-to-understand format.

# Installation
# Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/ai-code-reviewer.git
   cd ai-code-reviewer
   ```
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up your `.env` file:
   - Create a `.env` file in the root directory.
   - Add your Google Generative AI API key:
     ```plaintext
     API_KEY=your_google_api_key

## Usage
1. Run the Streamlit application:
   ```bash
   streamlit run app.py
2. Open your web browser and go to the provided local URL (e.g., `http://localhost:8501`).
3. Paste your Python code into the text area and click **Review Code**.
4. View the **Bug Report** and **Fixed Code** generated by the AI.