import duckdb
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Connect to the database and fetch aggregate data
print("Fetching supply chain data...")
con = duckdb.connect()
query = """
    SELECT
        CASE
            WHEN CAST(o.order_delivered_customer_date AS TIMESTAMP)  > CAST(o.order_estimated_delivery_date AS TIMESTAMP) THEN 'Late Deliveries'
            ELSE 'On-Time Deliveries'
        END AS delivery_status,
        AVG(i.freight_value) as avg_freight
    FROM 'data/olist_orders_dataset.csv' As o
    JOIN 'data/olist_order_items_dataset.csv' AS i
      ON o.order_id = i.order_id
    WHERE o.order_status = 'delivered'
      AND o.order_delivered_customer_date IS NOT NULL
    GROUP BY 1
"""
df = con.execute(query).df()

#2. Build the chart using Seaborn for professional styling
print("Generating executive visualization...")
plt.figure(figsize=(8, 6))

#Create a bar chart
sns.barplot(x='delivery_status', y='avg_freight' , hue='delivery_status', data=df, palette='crest', legend=False)

# Add titles and labels
plt.title('Average Shipping Cost: On-Time vs. Late Packages', fontsize=14, pad=15, fontweight='bold')
plt.xlabel('Status', fontsize=12)
plt.ylabel('Average Freight Cost ($)', fontsize=12)

# 3. Save the visualization locally
output_filename = 'delivery_cost_analysis.png'
plt.savefig(output_filename, bbox_inches='tight', dpi=300)

print(f"Sucess! The chart has been saved as '{output_filename}' in your main project folder.")


           