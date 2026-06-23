# Run Outputs for Project Scripts

This file captures terminal commands and their outputs for the main Python scripts in this repository.

## `python3 --version`

```bash
python3 --version
```
Python 3.10.4

---

## `python3 -m pip show streamlit`

```bash
python3 -m pip show streamlit
```
Name: streamlit
Version: 1.58.0
Summary: A faster way to build and share data apps
Home-page: https://streamlit.io
Author: 
Author-email: Snowflake Inc <hello@streamlit.io>
License-Expression: Apache-2.0
Location: /Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages
Requires: altair, anyio, blinker, cachetools, click, gitpython, httptools, itsdangerous, numpy, packaging, pandas, pillow, protobuf, pyarrow, pydeck, python-multipart, requests, starlette, tenacity, toml, typing-extensions, uvicorn, websockets
Required-by:

---

## `python3 -m pip show duckdb`

```bash
python3 -m pip show duckdb
```
Name: duckdb
Version: 1.5.3
Summary: DuckDB in-process database
Home-page: 
Author: DuckDB Foundation
Author-email: 
License: 
Location: /Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages
Requires: 
Required-by:

---

## `python3 -m pip show python-dotenv`

```bash
python3 -m pip show python-dotenv
```
Name: python-dotenv
Version: 1.2.2
Summary: Read key-value pairs from a .env file and set them as environment variables
Home-page: 
Author: 
Author-email: Saurabh Kumar <me+github@saurabh-kumar.com>
License: BSD-3-Clause
Location: /Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages
Requires: 
Required-by:

---

## `python3 -m pip show google-genai`

```bash
python3 -m pip show google-genai
```
Name: google-genai
Version: 2.8.0
Summary: GenAI Python SDK
Home-page: https://github.com/googleapis/python-genai
Author: 
Author-email: Google LLC <googleapis-packages@google.com>
License-Expression: Apache-2.0
Location: /Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages
Requires: anyio, distro, google-auth, httpx, pydantic, requests, sniffio, tenacity, typing-extensions, websockets
Required-by:

---

## `python3 -m py_compile src/dashboard.py`

```bash
python3 -m py_compile src/dashboard.py
```

---

## `python3 src/visualize_data.py`

```bash
python3 src/visualize_data.py
```
Fetching supply chain data...
Generating executive visualization...
Sucess! The chart has been saved as 'delivery_cost_analysis.png' in your main project folder.

---

## `python3 src/generate_pdf.py`

```bash
python3 src/generate_pdf.py
```
PDF  'Executive_Report.pdf'  created successfully!

---

## `python3 src/llm_reporting.py`

```bash
python3 src/llm_reporting.py
```
Warning: GEMINI_API_KEY not set. Export it before running this script.
Compiling Data and contacting the Large Language Model...

[System Note]: Connection failed (Reason: No API key was provided. Please pass a valid API key. Learn how to create an API key at https://ai.google.dev/gemini-api/docs/api-key.)
Warning: GEMINI_API_KEY not set. Export it before running this script.
Compiling Data and contacting the Large Language Model...

[System Note]: Connection failed (Reason: No API key was provided. Please pass a valid API key. Learn how to create an API key at https://ai.google.dev/gemini-api/docs/api-key.)

---

## `python3 src/predictive_model.py`

```bash
python3 src/predictive_model.py
```
Training the AI model...  (this might take a few seconds)
--- Machine Learning Model Results ---
Prediction Accuracy:  91.88%

---

## `python3 src/stats_analysis.py`

```bash
python3 src/stats_analysis.py
```
--- Statistical Analysis of Late Deliveries ---
Average Delay (Mean):               9.55 days
Typical Delay (Median):              5.81 days
Standard Deviation (volatility):    13.95 days
Worst Delay (Max):                  188.98 days

---

## `python3 src/data_pipeline.py`

```bash
python3 src/data_pipeline.py
```
Financial Impact of Delivery Performance:
  delivery_performance  total_orders  total_revenue  total_freight_cost
0              ON TIME        101475   1.206133e+07          2005441.45
1                 LATE          8714   1.158921e+06           192704.45

---

