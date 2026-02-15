import pandas as pd

customers_df = pd.DataFrame({
    'customer_id': [101, 102, 103, 104, 105],
    'customer_name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'customer_location': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
})

products_df = pd.DataFrame({
    'product_id': [201, 202, 203, 204, 205],
    'product_name': ['Laptop', 'Smartphone', 'Tablet', 'Headphones', 'Camera'],
    'category': ['Electronics', 'Electronics', 'Electronics', 'Accessories', 'Electronics'],
    'price': [1000, 500, 300, 50, 700] 
})

sales_df = pd.DataFrame({
    'customer_id': [101, 102, 103, 101, 104, 105, 102, 103],
    'product_id': [201, 202, 203, 204, 205, 201, 204, 202],
    'quantity_sold': [1, 2, 1, 3, 2, 1, 1, 2]
})


merged_sales_customers_df =  pd.merge(sales_df , customers_df , on = "customer_id" ,how = "left")
# print(merged_sales_customers_df)

final_df = pd.concat([merged_sales_customers_df, products_df], axis=1)
# print(final_df)

complete_sales_df = pd.merge(merged_sales_customers_df, products_df, on='product_id', how='left')
# print(complete_sales_df)

complete_sales_df['revenue'] = complete_sales_df['quantity_sold'] * complete_sales_df['price']
# print(complete_sales_df)

category_summary = complete_sales_df.groupby('category').agg({ 'quantity_sold': 'sum','revenue': 'sum'})
print(category_summary)
