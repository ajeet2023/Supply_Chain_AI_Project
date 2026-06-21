import duckdb
import pandas as pd
import numpy as np

#Connect to DucdDB database 
con = duckdb.connect()

#Step 1: SQL to grab only the late orders and their exact timestamps

query = """
    SELECT
        order_id,
        CAST(order_delivered_customer_date AS TIMESTAMP) AS actual_delivery,
        CAST(order_estimated_delivery_date AS TIMESTAMP) AS estimated_delivery
    FROM 'data/olist_orders_dataset.csv'
    WHERE order_status = 'delivered'
      AND order_delivered_customer_date IS NOT NULL
      AND order_estimated_delivery_date IS NOT NULL
      AND CAST(order_delivered_customer_date AS TIMESTAMP) > CAST(order_estimated_delivery_date AS TIMESTAMP)
"""

#Now python knoows exactly what 'con' is and when it hits this line
df = con.execute(query).df()

df['days_late'] = (df['actual_delivery'] - df['estimated_delivery']).dt.total_seconds() / (24 * 3600)

mean_delay = np.mean(df['days_late'])
median_delay = np.median(df['days_late'])
std_dev = np.std(df['days_late'])
max_delay = np.max(df['days_late'])

print("--- Statistical Analysis of Late Deliveries ---")
print(f"Average Delay (Mean):               {mean_delay:.2f} days")      
print(f"Typical Delay (Median):              {median_delay:.2f} days")
print(f"Standard Deviation (volatility):    {std_dev:.2f} days")
print(f"Worst Delay (Max):                  {max_delay:.2f} days")
