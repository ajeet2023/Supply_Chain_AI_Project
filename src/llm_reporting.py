import os
from dotenv import load_dotenv
from google import genai


def load_api_key():
    load_dotenv()
    gemini_key = os.getenv("GEMINI_API_KEY")
    if gemini_key:
        os.environ["GEMINI_API_KEY"] = gemini_key
        return True

    print("Warning: GEMINI_API_KEY not set. Export it before running this script.")
    return False


def build_prompt(model_accuracy=91.94, average_delay=2.5, late_revenue=150000):
    return f"""
You are a Senior Data Scientist writing a brief executive email to the VP of Supply Chain.

Context:
We just deployed a new data pipeline and machine learning model to predict late deliveries before they leave the warehouse.

Here are the actual metrics from today's pipeline run:

- Total Revenue sitting in 'late' status: ${late_revenue:,}
- Average Delay for late packages: {average_delay} days
- Predictive AI Model Accuracy: {model_accuracy} %

Task:
Write a concise, professional 3-paragraph email summarizing these findings.
Tone should be objective and solution-oriented.
End by recommending that the warehouse routing team begins utilizing the new AI predictions to prioritize high-risk packages.
"""


def generate_email(prompt: str) -> str:
    client = genai.Client()
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )
    return response.text


def main():
    load_api_key()
    print("Compiling Data and contacting the Large Language Model...")

    prompt = build_prompt()
    try:
        response_text = generate_email(prompt)
        print("\n================ EXECUTIVE EMAIL DRAFT ================\n")
        print(response_text)
        print("\n========================================================")
    except Exception as e:
        print(f"\n[System Note]: Connection failed (Reason: {e})")


if __name__ == "__main__":
    main()
    
