import os
from google import genai

# Load the API key from the environment instead of hard-coding it here.
# Do NOT commit secrets to version control. Set GEMINI_API_KEY in your shell or
# in a local .env file (and ensure .env is in .gitignore).
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if GEMINI_API_KEY:
    os.environ["GEMINI_API_KEY"] = GEMINI_API_KEY
else:
    print("Warning: GEMINI_API_KEY not set. Export it before running this script.")

# 1. The Data Context (Injecting metrics)
model_accuracy = 91.94
average_delay = 2.5
late_revenue = 150000

#2 Prompt Engineering 
prompt = f"""
You are a Senior Data Scientist writing a brief executive email to the VP of Supply Chain.

Context:
We just deployed a new data pipeline and machine learning model to predict late deliveries before they leave the warehouse,

Here are the actual metrics from today's pipline run:

-Total Revenue sitting in 'late' status: ${late_revenue:,}
- Average Delay for late packages: {average_delay} days
- Predictive AI Model Accuracy: {model_accuracy} %

Task:
Write a concise, professional 3-paragraph email summarizing these findings.
Tone should be objective and solution-oriented.
End by recommending that the warehouse routing team begins utilizing the new AI preictions to priortize high-risk packages.
"""

# 3. Call the LLM using the modern google.genai SDK
print("Compiling Data and contacting the Large Language Model...")

try:
    client = genai.Client()

    response = client.models.generate_content(
        model= 'gemini-2.5-flash',
        contents=prompt
    )

    print("\n================ EXECUTIVE EMAIL DRAFT ================\n")
    print(response.text)
    print("\n========================================================")

except Exception as e:
    print(f"\n[System Note]: Connection failed (Reason: {e})")
import os
from google import genai

# Load the API key from the environment instead of hard-coding it here.
# Do NOT commit secrets to version control. Set GEMINI_API_KEY in your shell or
# in a local .env file (and ensure .env is in .gitignore).
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if GEMINI_API_KEY:
    os.environ["GEMINI_API_KEY"] = GEMINI_API_KEY
else:
    print("Warning: GEMINI_API_KEY not set. Export it before running this script.")

# 1. The Data Context (Injecting metrics)
model_accuracy = 91.94
average_delay = 2.5
late_revenue = 150000

#2 Prompt Engineering 
prompt = f"""
You are a Senior Data Scientist writing a brief executive email to the VP of Supply Chain.

Context:
We just deployed a new data pipeline and machine learning model to predict late deliveries before they leave the warehouse,

Here are the actual metrics from today's pipline run:

-Total Revenue sitting in 'late' status: ${late_revenue:,}
- Average Delay for late packages: {average_delay} days
- Predictive AI Model Accuracy: {model_accuracy} %

Task:
Write a concise, professional 3-paragraph email summarizing these findings.
Tone should be objective and solution-oriented.
End by recommending that the warehouse routing team begins utilizing the new AI preictions to priortize high-risk packages.
"""

# 3. Call the LLM using the modern google.genai SDK
print("Compiling Data and contacting the Large Language Model...")

try:
    # Because we used os.environ above, we can leave the parantheses completely empty here!
    client = genai.Client()

    #Generate content using the current stnadard model 
    response = client.models.generate_content(
        model= 'gemini-2.5-flash',
        contents=prompt
    )

    print("\n================ EXECUTIVE EMAIL DRAFT ================\n")
    print(response.text)
    print("\n========================================================")

except Exception as e:
    print(f"\n[System Note]: Connection failed (Reason: {e})")
    
