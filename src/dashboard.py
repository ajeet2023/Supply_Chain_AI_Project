import streamlit as st
import os
from google import genai
from dotenv import load_dotenv

# Run locally with:
#   streamlit run src/dashboard.py
# If you want to test on a specific port:
#   streamlit run src/dashboard.py --server.port 8501

# Load the environment variables from hidden .env file
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Configure the web page settings
st.set_page_config(page_title="Supply Chain AI", layout="wide")

st.title("📦 Supply Chain AI Command Center")
st.markdown("Welcome to the executive dashboard for predictive delivery analytics.")

st.divider()

#1. Display the Metrics
st.header("1. Real-Time Pipline Metrics")
col1, col2, col3 = st.columns(3)
col1.metric("model Accuracy", "91.84", "+1.2%")
col2.metric("Revenue at Risk", "$150,000", "Critical")

st.divider()

#2. Display the visualization
st.header("2. Freight Cost Analysis")
st.markdown("This visualization was generated directly from our local DuckDB database.")
try:
    #this looks for the exact image we generated in Phase 6
    st.image("delivery_cost_analysis.png", width=700)
except FileNotFoundError:
    st.warning("Chart not found. Make sure 'delivery_cost_analysis,png' is in your main project folder.")

st.divider()

#3. Interactive AI Generation
st.header("3. AI Executive Summary")
st.markdown("Click below to trigger the Generative AI model to draft an email based on current metrics.")

if st.button("Generate Executive Email"):
    with st.spinner("Contacting Google Gemini AI..."):
        try:
            prompt = """
            You are a Senior Data Scientist writing a brief executive email to the VP of Supply Chain.
            Metrics: Revenue at risk is $150,000, Average Delay is 2.5 days, Model Accuracy is 91.84%.
            Task: Write a concise, professional 3-paragraph email summarizing these findings.
            Tone: Objective and solution-oriented.
            """

            response_text = ""
            if not GEMINI_API_KEY:
                st.error("GEMINI_API_KEY is not configured. Set it in Streamlit Cloud secrets or in a local .env file.")
            else:
                client = genai.Client()
                response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=prompt
                )

                response_text = response.text
                st.success("Draft generated successfully!")

            if response_text:
                st.text_area("Executive Email Draft", response_text, height=300)

        except Exception as e:
            st.error(f"Connection failed: {e}")

