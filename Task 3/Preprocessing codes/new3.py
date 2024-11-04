import pandas as pd

# Load the CSV file
file_path = '/Users/prana/Documents/My Tableau Prep Repository/Datasources/Output 6.csv'
df = pd.read_csv(file_path)

# Sort the data by CO2 emissions in descending order
df_sorted = df.sort_values(by='CO2_emisions', ascending=False)

# Get the top 10 rows
df_top10 = df_sorted.head(10)

# Save the top 10 rows to a new CSV file
output_file_path = '/Users/prana/Documents/My Tableau Prep Repository/Datasources/Output 6_new1.csv'
df_top10.to_csv(output_file_path, index=False)

print("Top 10 rows saved to:", output_file_path)
