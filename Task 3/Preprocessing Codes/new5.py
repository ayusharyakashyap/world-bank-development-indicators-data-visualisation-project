import pandas as pd

# Load the CSV file
file_path = '/Users/prana/Documents/My Tableau Prep Repository/Datasources/Output 6.csv'
df = pd.read_csv(file_path)

# Sort the data by electric power consumption in descending order
df_sorted_power = df.sort_values(by='electric_power_consumption', ascending=False)

# Get the top 10 rows based on electric power consumption
df_top10_power = df_sorted_power.head(10)

# Save the top 10 rows to a new CSV file
output_file_path_power = '/Users/prana/Documents/My Tableau Prep Repository/Datasources/Output 6_top10_power.csv'
df_top10_power.to_csv(output_file_path_power, index=False)

print("Top 10 rows based on electric power consumption saved to:", output_file_path_power)
