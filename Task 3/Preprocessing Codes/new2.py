import pandas as pd

# Load the CSV file
file_path = '/Users/prana/Documents/My Tableau Prep Repository/Datasources/Output 6.csv'
df = pd.read_csv(file_path)

# Sort the DataFrame by CO2 emissions in descending order
df_sorted = df.sort_values(by='CO2_emisions', ascending=False)

# Classify the first 10 rows as 'Top 10' and the rest as 'Others'
df_sorted['Category'] = ['Top 10' if i < 10 else 'Others' for i in range(len(df_sorted))]

# Calculate the total CO2 emissions for all rows
total_co2_emissions = df_sorted['CO2_emisions'].sum()

# Calculate the total CO2 emissions for the top 10 rows
total_co2_top_10 = df_sorted.head(10)['CO2_emisions'].sum()

# Group by the category and calculate the aggregate (sum) of all other columns
# Assuming you want to sum the other columns, excluding 'Category'
aggregate_columns = df.columns.drop(['CO2_emisions'])  # Exclude CO2_emissions column
aggregated_df = df_sorted.groupby('Category').agg({col: 'sum' for col in aggregate_columns})

# Add the total CO2 emissions to the aggregated DataFrame
aggregated_df['Total_CO2_Emissions'] = df_sorted.groupby('Category')['CO2_emisions'].sum()

# Output the aggregated result to a new CSV file
output_file_path = '/Users/prana/Documents/My Tableau Prep Repository/Datasources/Output 6_new.csv'
aggregated_df.to_csv(output_file_path)

print(f"Total CO2 Emissions for all rows: {total_co2_emissions}")
print(f"Total CO2 Emissions for top 10 rows: {total_co2_top_10}")
print(f"Aggregated data has been saved to: {output_file_path}")
