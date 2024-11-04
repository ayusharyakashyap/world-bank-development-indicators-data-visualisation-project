import pandas as pd

# Load the CSV file
file_path = '/Users/prana/Documents/My Tableau Prep Repository/Datasources/Output 6.csv'
df = pd.read_csv(file_path)

# Sort the DataFrame by CO2 emissions in descending order (same as before)
df_sorted = df.sort_values(by='CO2_emisions', ascending=False)

# Classify the first 10 rows as 'Top 10' and the rest as 'Others' (same as before)
df_sorted['Category'] = ['Top 10' if i < 10 else 'Others' for i in range(len(df_sorted))]

# Calculate the total CO2 emissions for all rows (same as before)
# total_co2_emissions = df_sorted['CO2_emisions'].sum()

# Calculate the total CO2 emissions for the top 10 rows (same as before)
# total_co2_top_10 = df_sorted.head(10)['CO2_emisions'].sum()

# Now calculate greenhouse gas emissions for the top 10 and others
# Assuming there is a column named 'GHG_emisions' for greenhouse gases
total_ghg_emissions = df_sorted['other_greenhouse_emisions'].sum()  # Total for all countries
total_ghg_top_10 = df_sorted[df_sorted['Category'] == 'Top 10']['other_greenhouse_emisions'].sum()  # Total for top 10 countries

# Output the total GHG emissions as well
output_file_path = '/Users/prana/Documents/My Tableau Prep Repository/Datasources/Output 6_new2.csv'
df_sorted.to_csv(output_file_path, index=False)  # Save sorted data to a new CSV file

# print(f"Total CO2 Emissions for all rows: {total_co2_emissions}")
# print(f"Total CO2 Emissions for top 10 rows: {total_co2_top_10}")
print(f"Total GHG Emissions for all rows: {total_ghg_emissions}")
print(f"Total GHG Emissions for top 10 rows: {total_ghg_top_10}")
print(f"Sorted data with categories has been saved to: {output_file_path}")
