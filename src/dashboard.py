import streamlit as st
import os
from google import genai
from dotenv import load_dotenv

# Run locally with:
#   streamlit run src/dashboard.py
# If you want to test on a specific port:
#   streamlit run src/dashboard.py --server.port 8501

def get_gemini_api_key():
    load_dotenv()

    env_key = os.getenv("GEMINI_API_KEY")
    if env_key:
        return env_key, "local .env"

    secret_key = st.secrets.get("GEMINI_API_KEY")
    if secret_key:
        return secret_key, "Streamlit secrets (top-level)"

    google_secret = st.secrets.get("google", {}).get("GEMINI_API_KEY")
    if google_secret:
        return google_secret, "Streamlit secrets (google.GEMINI_API_KEY)"

    gemini_secret = st.secrets.get("gemini", {}).get("api_key")
    if gemini_secret:
        return gemini_secret, "Streamlit secrets (gemini.api_key)"

    return None, None

GEMINI_API_KEY, key_source = get_gemini_api_key()
if GEMINI_API_KEY:
    os.environ["GEMINI_API_KEY"] = GEMINI_API_KEY

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

if GEMINI_API_KEY:
    st.success(f"AI key status: configured via {key_source}.")
else:
    st.error(
        "AI key status: GEMINI_API_KEY is not configured. Add it to Streamlit Cloud secrets or create a local .env file with GEMINI_API_KEY."
    )
    st.write("Streamlit secrets keys found:")
    st.json({
        "has_GEMINI_API_KEY": "GEMINI_API_KEY" in st.secrets,
        "has_google_GEMINI_API_KEY": "GEMINI_API_KEY" in st.secrets.get("google", {}),
        "has_gemini_api_key": "api_key" in st.secrets.get("gemini", {}),
    })

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
                st.error(
                    "GEMINI_API_KEY is not configured. Add it to Streamlit Cloud secrets or create a local .env file with GEMINI_API_KEY."
                )
            else:
                client = genai.Client(api_key=GEMINI_API_KEY)
                st.write(f"Using GEMINI_API_KEY from {key_source}.")
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

