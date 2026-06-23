# Run Outputs for Project Scripts

This file captures terminal commands and their outputs for the main Python scripts in this repository. It is safe for GitHub and helps show what happens when each script is executed.

## Python environment

```bash
python3 --version
```
$(python3 --version 2>&1)

```bash
python3 -m pip show streamlit
```
$(python3 -m pip show streamlit 2>&1 || echo 'streamlit not installed')

```bash
python3 -m pip show duckdb
```
$(python3 -m pip show duckdb 2>&1 || echo 'duckdb not installed')

```bash
python3 -m pip show python-dotenv
```
$(python3 -m pip show python-dotenv 2>&1 || echo 'python-dotenv not installed')

```bash
python3 -m pip show google-genai
```
$(python3 -m pip show google-genai 2>&1 || echo 'google-genai not installed')

---

## `python3 src/dashboard.py`

```bash
python3 src/dashboard.py
```
$(python3 src/dashboard.py 2>&1 | sed 's/\x1b\[[0-9;]*m//g')

---

## `python3 src/visualize_data.py`

```bash
python3 src/visualize_data.py
```
$(python3 src/visualize_data.py 2>&1 | sed 's/\x1b\[[0-9;]*m//g')

---

## `python3 src/generate_pdf.py`

```bash
python3 src/generate_pdf.py
```
$(python3 src/generate_pdf.py 2>&1 | sed 's/\x1b\[[0-9;]*m//g')

---

## `python3 src/llm_reporting.py`

```bash
python3 src/llm_reporting.py
```
$(python3 src/llm_reporting.py 2>&1 | sed 's/\x1b\[[0-9;]*m//g')

---

## `python3 src/predictive_model.py`

```bash
python3 src/predictive_model.py
```
$(python3 src/predictive_model.py 2>&1 | sed 's/\x1b\[[0-9;]*m//g')

---

## `python3 src/stats_analysis.py`

```bash
python3 src/stats_analysis.py
```
$(python3 src/stats_analysis.py 2>&1 | sed 's/\x1b\[[0-9;]*m//g')

---

## `python3 src/data_pipeline.py`

```bash
python3 src/data_pipeline.py
```
$(python3 src/data_pipeline.py 2>&1 | sed 's/\x1b\[[0-9;]*m//g')
