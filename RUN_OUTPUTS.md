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
Compiling Data and contacting the Large Language Model...

[System Note]: Connection failed (Reason: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}})

---

## `python3 src/predictive_model.py`

```bash
python3 src/predictive_model.py
```
Training the AI model...  (this might take a few seconds)
--- Machine Learning Model Results ---
Prediction Accuracy:  91.91%

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

================================================
STEP 1: Preview first 5 rows from orders dataset
================================================

                           order_id  ... order_estimated_delivery_date
0  e481f51cbdc54678b7cc49136f2d6af7  ...                    2017-10-18
1  53cdb2fc8bc7dce0b6741e2150273451  ...                    2018-08-13
2  47770eb9100c2d0c44946d9cf07ec65d  ...                    2018-09-04
3  949d5b44dbf5de918fe9c16f97b45f8a  ...                    2017-12-15
4  ad21c59c0840e6cb83a9ceb5573f8159  ...                    2018-02-26

[5 rows x 8 columns]

=================================================================
STEP 2: Sample delivery performance for first 10 delivered orders
=================================================================

                           order_id  ... delivery_performance
0  e481f51cbdc54678b7cc49136f2d6af7  ...              ON TIME
1  53cdb2fc8bc7dce0b6741e2150273451  ...              ON TIME
2  47770eb9100c2d0c44946d9cf07ec65d  ...              ON TIME
3  949d5b44dbf5de918fe9c16f97b45f8a  ...              ON TIME
4  ad21c59c0840e6cb83a9ceb5573f8159  ...              ON TIME
5  a4591c265e18cb1dcee52889e2d8acc3  ...              ON TIME
6  6514b8ad8028c9f2cc2374ded245783f  ...              ON TIME
7  76c6e866289321a7c93b82b54852dc33  ...              ON TIME
8  e69bfb5eb88e0ed6a785585b27e16dbf  ...              ON TIME
9  e6ce16cb79ec1d90b1da9085a6118aeb  ...              ON TIME

[10 rows x 4 columns]

==================================================
STEP 3: Join orders with order item financial data
==================================================

                           order_id order_status   price  freight_value
0  e481f51cbdc54678b7cc49136f2d6af7    delivered   29.99           8.72
1  53cdb2fc8bc7dce0b6741e2150273451    delivered  118.70          22.76
2  47770eb9100c2d0c44946d9cf07ec65d    delivered  159.90          19.22
3  949d5b44dbf5de918fe9c16f97b45f8a    delivered   45.00          27.20
4  ad21c59c0840e6cb83a9ceb5573f8159    delivered   19.90           8.72
5  a4591c265e18cb1dcee52889e2d8acc3    delivered  147.90          27.36
6  136cce7faa42fdb2cefd53fdc79a6098     invoiced   49.90          16.05
7  6514b8ad8028c9f2cc2374ded245783f    delivered   59.99          15.17
8  76c6e866289321a7c93b82b54852dc33    delivered   19.90          16.05
9  e69bfb5eb88e0ed6a785585b27e16dbf    delivered  149.99          19.77

==========================================================
STEP 4: Aggregate financial impact by delivery performance
==========================================================

  delivery_performance  total_orders  total_revenue  total_freight_cost
0              ON TIME        101475   1.206133e+07          2005441.45
1                 LATE          8714   1.158921e+06           192704.45

---

