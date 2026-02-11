import pandas as pd
import numpy as np

df1 = pd.read_csv("world_alcohol_consumption_1.csv")
df2 = pd.read_csv("world_alcohol_consumption_2.csv")

df1.columns = df1.columns.str.strip()
df2.columns = df2.columns.str.strip()

df1['Price'] = np.random.randint(1, 30, size=len(df1))

df2['Brand'] = np.random.choice(
    ['Brand_A', 'Brand_B', 'Brand_C', 'Brand_D', 'Brand_E'],
    size=len(df2)
)

total_individuals = df1['Count'].sum()

gender_representation = df1['Gender'].value_counts()

gender_counts = df1.groupby('Gender')['Count'].sum()

unique_countries = df2['Countries'].nunique()

highest_consumption_country = (
    df2.groupby('Countries')['Display Value']
    .sum()
    .idxmax()
)

merged_df = pd.merge(
    df1,
    df2,
    left_on='Country',
    right_on='Countries',
    how='inner'
)

average_display_value_by_region_df = (
    merged_df.groupby('WHO Region')['Display Value']
    .mean()
    .reset_index()
)

region_gender_avg = (
    merged_df.groupby(['WHO Region', 'Gender'])['Display Value']
    .mean()
)

df2['Date'] = pd.to_datetime(df2['Date'])
df2['Month'] = df2['Date'].dt.month
df2['Year'] = df2['Date'].dt.year

month_max_sales = (
    df2.groupby('Month')['Count']
    .sum()
    .idxmax()
)

top_brand_in_max_month = (
    df2[df2['Month'] == month_max_sales]
    .groupby('Brand')['Count']
    .sum()
    .idxmax()
)

last_year = df2['Year'].max()

top_5_brands_last_year = (
    df2[df2['Year'] == last_year]
    .groupby(['Brand', 'Countries'])['Count']
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

who_limit = 5

countries_exceeding_who = (
    df1.groupby('Country')['Display Value']
    .mean()
)

countries_exceeding_who = countries_exceeding_who[countries_exceeding_who > who_limit]
