# import duckdb
# # 1. Connect to an in-memory DuckDB database
# con = duckdb.connect()
# # 2. Write our first SQL query
# # We are querying the CSV file directly to see the first 5 rows
# query = """
# SELECT * FROM 'data/olist_orders_dataset.csv' 
# LIMIT 5;
# """
# # 3. Execute the SQL and fetch the results as a DataFrame
# #(A DataFrame is just a fancy python word for a data table)
# results = con.execute(query).df()
# # 4. Print the results to the screen
# print("Here are the first 5 rows of our orders data:")
# print(results)

# import duckdb
# # Connect to the DuckDB datbase
# con = duckdb.connect()

# # Advanced SQL: CTEs, Date Casting, and CASE Statements
# query = """
#     WITH DeliveryData AS(
#         SELECT
#             order_id,
#             CAST(order_delivered_customer_date AS TIMESTAMP) AS actual_delivery,
#             CAST(order_estimated_delivery_date AS TIMESTAMP) AS estimated_delivery
#         FROM 'data/olist_orders_dataset.csv'
#         WHERE order_status = 'delivered'
#            AND order_delivered_customer_date IS NOT NULL

#     )
#     SELECT
#         order_id,
#         actual_delivery,
#         estimated_delivery,
#         CASE
#             WHEN actual_delivery > estimated_delivery THEN 'LATE'
#             ELSE 'ON TIME'
#         END AS delivery_performance
#     FROM DeliveryData
#     LIMIT 10;
# """

# # Execute and fetch results
# result = con.execute(query).df()

# print("Delivery performance Analysis (First 10 Orders):")
# print(result)

# import duckdb
# con = duckdb.connect()

# # Advanced SQL: INNER JOIN connecting two diffrent CSV files
# query = """
#     SELECT
#         o.order_id,
#         o.order_status,
#         i.price,
#         i.freight_value
#     FROM 'data/olist_orders_dataset.csv' AS o
#      JOIN 'data/olist_order_items_dataset.csv' AS i
#        ON o.order_id = i.order_id
#     LIMIT 10;
# """
# result = con.execute(query).df()
# print("Joined order and Financial Data:")
# print(result)

import duckdb

con = duckdb.connect()

#Advanced SQL: CTE + Join + Group BY Aggregation
query = """
    WITH DeliveryData AS (
        SELECT
            order_id,
            CASE
                WHEN CAST(order_delivered_customer_date AS TIMESTAMP) > CAST(order_estimated_delivery_date AS TIMESTAMP) THEN 'LATE'
                ELSE 'ON TIME'
            END AS delivery_performance
        FROM 'data/olist_orders_dataset.csv'
        WHERE order_status = 'delivered'
           AND order_delivered_customer_date IS NOT NULL
    )
SELECT
    d.delivery_performance,
    COUNT(d.order_id) AS total_orders,
    SUM(CAST(i.price AS DOUBLE)) AS total_revenue,
    SUM(CAST(i.freight_value AS DOUBLE)) AS total_freight_cost
FROM DeliveryData AS d
JOIN 'data/olist_order_items_dataset.csv' AS i
    ON d.order_id = i.order_id
GROUP BY d.delivery_performance;
"""

result = con.execute(query).df()
print("Financial Impact of Delivery Performance:")
print(result)