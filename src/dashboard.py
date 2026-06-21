import streamlit as st
import os
from google import genai
from dotenv import load_dotenv

# Load the enivronment variables from hidden .env file
load_dotenv()

#Configure the web page settings
st.set_page_config(page_title="Supply Chain AI", layout="wide")

st.title("📦 Supply Chain AI Command Center")
st.markdown("Welcome to the execuitive dashboard for predictive delivery analytics.")

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
            Metrics: Revenu at risk is $150,000, Average Delay is 2.5 days, Model Accuracy is 91.84%.
            Task: Write a concise, professional 3-paragraph email summarizing these findings.
            Tone: Objective and solution-oriented.
            """

            # The client will now automatically find my key from the loaded .env file!
            client = genai.Client()
            response = client.models.generate_content(
                model='gemini-2.5-flash' ,
                contents=prompt
            )

            st.success("Draft generated successfully!")

            # Display the AI response in a clean, scrollable text box
            st.text_area("Executive Email Draft", response.text, height=300)

        except Exception as e:
            st.error(f"Connection failed: {e}")

