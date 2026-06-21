
import duckdb
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

#1. Connect and fetch the training data
con = duckdb.connect()
query = """
    SELECT 
         i.price,
         1.freight_value,
         CASE
            WHEN CAST(o.order_delivered_customer_date AS TIMESTAMP) > CAST(o.order_estimated_delivery_date AS TIMESTAMP) THEN 1
            ELSE 0
         END AS is_late
    FROM 'data/olist_orders_dataset.csv' AS o
    JOIN 'data/olist_order_items_dataset.csv' AS i
    ON o.order_id = i.order_id
    WHERE o.order_status = 'delivered'
      AND o.order_delivered_customer_date IS NOT NULL
      
"""
df = con.execute(query).df()

#2.  Prepare the Data for the AI
#X = The features the AI will use to guess (Price and Freight Value)
#Y = The exact answer we want the AI to learn (1 for late, 0 for on-Time)
X = df[['price', 'freight_value']]
Y = df['is_late']

# We split the data: 80% to train the AI, 20% to test it blindly
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

#3. Train the Machine Learning Model (Random Forest Algorithm)
print("Training the AI model...  (this might take a few seconds)")
model = RandomForestClassifier(random_state=42)
model.fit(X_train, Y_train)

# 4. Test the AI on the 20% of data it hasn't seen
predictions = model.predict(X_test)

# 5. Grade the AI's performance
accuracy = accuracy_score(Y_test, predictions)
print("--- Machine Learning Model Results ---")
print(f"Prediction Accuracy:  {accuracy * 100:.2f}%")
