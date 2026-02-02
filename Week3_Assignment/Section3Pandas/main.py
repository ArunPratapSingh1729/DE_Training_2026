import pandas as pd

df1 = pd.read_csv("world_alcohol_consumption_1.csv")
df2 = pd.read_csv("world_alcohol_consumption_2.csv")

total_count = df2['Count'].sum()

gender_counts = df2.groupby('Gender')['Count'].sum()

unique_countries = df2['Countries'].nunique()

highest_consumption_country = (df1.groupby('Country')['Display Value'].sum().idxmax())

merged_df = pd.merge( df1, df2, left_on='Country', right_on='Countries', how='inner')

average_display_value_by_region_df = (merged_df.groupby('WHO region')['Display Value'].mean().reset_index())

gender_region_consumption = (merged_df.groupby(['WHO region', 'Gender'])['Display Value'].mean().reset_index())

df1['Price'] = [10.0] * len(df1)
df1['Brand'] = df1['Beverage Types']

df1['Year'] = df1['Year'].astype(int)

max_year = df1['Year'].max()

max_brand_month = (df1[df1['Year'] == max_year].groupby('Brand')['Display Value'].sum().idxmax())

top_5_brands = (df1[df1['Year'] == max_year].groupby(['Brand', 'Country'])['Display Value'].sum().reset_index().sort_values('Display Value', ascending=False).head(5))


who_limit = df1['Display Value'].mean()
countries_exceeding_who = (
    df1.groupby('Country')['Display Value']
       .mean()
       .reset_index()
)
countries_exceeding_who = countries_exceeding_who[
    countries_exceeding_who['Display Value'] > who_limit
]


