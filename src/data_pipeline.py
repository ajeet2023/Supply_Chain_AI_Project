"""Run this script from the project root to display all data pipeline steps in the terminal.

Usage:
    python3 src/data_pipeline.py
"""

import duckdb


def print_section(title: str) -> None:
    border = '=' * len(title)
    print(f"\n{border}")
    print(title)
    print(f"{border}\n")


def run_preview_orders(con):
    print_section('STEP 1: Preview first 5 rows from orders dataset')
    query = """
        SELECT *
        FROM 'data/olist_orders_dataset.csv'
        LIMIT 5;
    """
    df = con.execute(query).df()
    print(df)


def run_delivery_performance_sample(con):
    print_section('STEP 2: Sample delivery performance for first 10 delivered orders')
    query = """
        WITH DeliveryData AS (
            SELECT
                order_id,
                CAST(order_delivered_customer_date AS TIMESTAMP) AS actual_delivery,
                CAST(order_estimated_delivery_date AS TIMESTAMP) AS estimated_delivery
            FROM 'data/olist_orders_dataset.csv'
            WHERE order_status = 'delivered'
              AND order_delivered_customer_date IS NOT NULL
              AND order_estimated_delivery_date IS NOT NULL
        )
        SELECT
            order_id,
            actual_delivery,
            estimated_delivery,
            CASE
                WHEN actual_delivery > estimated_delivery THEN 'LATE'
                ELSE 'ON TIME'
            END AS delivery_performance
        FROM DeliveryData
        LIMIT 10;
    """
    df = con.execute(query).df()
    print(df)


def run_joined_financial_data(con):
    print_section('STEP 3: Join orders with order item financial data')
    query = """
        SELECT
            o.order_id,
            o.order_status,
            i.price,
            i.freight_value
        FROM 'data/olist_orders_dataset.csv' AS o
        JOIN 'data/olist_order_items_dataset.csv' AS i
          ON o.order_id = i.order_id
        LIMIT 10;
    """
    df = con.execute(query).df()
    print(df)


def run_aggregated_financial_impact(con):
    print_section('STEP 4: Aggregate financial impact by delivery performance')
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
              AND order_estimated_delivery_date IS NOT NULL
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
    df = con.execute(query).df()
    print(df)


def main():
    con = duckdb.connect()
    run_preview_orders(con)
    run_delivery_performance_sample(con)
    run_joined_financial_data(con)
    run_aggregated_financial_impact(con)


if __name__ == '__main__':
    main()
