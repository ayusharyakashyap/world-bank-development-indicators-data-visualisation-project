import pandas as pd

# Load the CSV file
file_path = '/Users/prana/Documents/My Tableau Prep Repository/Datasources/Output 6.csv'
data = pd.read_csv(file_path)

# Display the first few rows to understand the structure of the file
data.head()

# Sort the data by CO2_emisions in descending order
sorted_data = data.sort_values(by='CO2_emisions', ascending=False)

# Calculate the total CO2 emissions for all rows
total_co2_emissions = sorted_data['CO2_emisions'].sum()

# Calculate the total CO2 emissions for the top 10 rows
top_10_co2_emissions = sorted_data.head(10)['CO2_emisions'].sum()

print(total_co2_emissions)
print(top_10_co2_emissions)

