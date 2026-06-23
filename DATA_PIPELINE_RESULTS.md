# Data Pipeline Results

Run this from the project root:

```bash
python3 src/data_pipeline.py
```

## Output

```text
================================================
STEP 1: Preview first 5 rows from orders dataset
================================================

                           order_id  ... order_estimated_delivery_date
0  e481f51cbdc54678b7cc49136f2d6af7  ...                    2017-10-18
1  53cdb2fc8bc7dce0b6741e2150273451  ...                    2018-08-13
2  47770eb9100c2d0c44946d9cf07ec65d  ...                    2018-09-04
3  949d5b44dbf5de918fe9c16f97b45f8a    ...                    2017-12-15
4  ad21c59c0840e6cb83a9ceb5573f8159  ...                    2018-02-26

[5 rows x 8 columns]

=================================================================
STEP 2: Sample delivery performance for first 10 delivered orders
=================================================================

                           order_id  ... delivery_performance
0  e481f51cbdc54678b7cc49136f2d6af7  ...              ON TIME
1  53cdb2fc8bc7dce0b6741e2150273451  ...              ON TIME
2  47770eb9100c2d0d0c44946d9cf07ec65d  ...              ON TIME
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
0                 LATE          8714   1.158921e+06           192704.45
1              ON TIME        101475   1.206133e+07          2005441.45
```
