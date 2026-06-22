# Deploying to Streamlit Community Cloud

## Requirements
- `streamlit.toml` in the repository root
- `requirements.txt` with all dependencies
- `src/dashboard.py` as the Streamlit app entry point
- a GitHub account connected to Streamlit Cloud

## Deployment steps
1. Push your changes to GitHub:
   ```bash
git add .
git commit -m "Prepare app for Streamlit Cloud"
git push origin main
```
2. Go to https://share.streamlit.io and sign in with GitHub.
3. Click **New app**.
4. Select your repository: `ajeet2023/Supply_Chain_AI_Project`.
5. Set the branch to `main`.
6. Set the file path to `src/dashboard.py`.
7. Click **Deploy**.

## Secrets
- Open the Streamlit app dashboard, go to **Settings** → **Secrets**.
- Add the following secret:
  - `GEMINI_API_KEY`: your Google Gemini API key

## Notes
- Do not commit `.env`.
- If the app fails to start, check the Streamlit Cloud logs.
