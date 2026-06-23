📦 **Supply Chain AI Command Center**

An automated, end-toe-end supply chain analytics pipeline that leverages machine learning and generative AI to provide actionable execuitive insights.

🚀 **Overview**

This project moves beyond standard BI dashboards by automating the data-to-decision pipeline. It processes supply chain telemetry, perform predictive cost analysis, and generates context-aware executive summaries using the Google Gemini AI

🛠️ **Tech Stack**

**Dashbaording**: Streamlit(interactive Frontend)
**Data Engineering:** DuckDB (High-performance analytical Fronted)
**Visualization** Seaborn & Matplotlib (Automated visual reporting)
**AI/LLM** Google Gemini API (Natural language executive synthesis)
**Reporting** ReportLab (Automated PDF generation)
**Security** Environment-variable managment (python-dotenv)

⚙️ **Key Features**
**Automated Data Processing: ETL pipeline that cleans and processes raw supply chain logs.

**Predictive Insights** ML-driven analysis to forecast delivery costs.

**AI-Powered Synthesis** Generates human-readable executive summaries, translating complex data into business strategy.

**Professional Reporting** Instant generation of formal PDF reports with embedded data visualizations.

🔐 **Security First** 

This project implements roubust security practicies, including the use of .env files for credential management and .gitignore protocols to ensure API keys are never exposed in version control.

## Run the dashboard locally

From the repository root, open a terminal and run:

```bash
pip install -r requirements.txt
streamlit run src/dashboard.py
```

Then open the browser at `http://localhost:8501`.

If you are running on a hosted service like Streamlit Community Cloud, set the app path to `src/dashboard.py`.


## Data Pipeline Results

[![Data Pipeline Results](https://img.shields.io/badge/Data%20Pipeline-Results-blue?style=flat-square)](DATA_PIPELINE_RESULTS.md)

The full terminal output from `python3 src/data_pipeline.py` is available in `DATA_PIPELINE_RESULTS.md`.

## Full Script Run Outputs

[![Run Outputs](https://img.shields.io/badge/Run%20Outputs-MD-green?style=flat-square)](RUN_OUTPUTS.md)

The full terminal outputs for each script are available in `RUN_OUTPUTS.md`.
