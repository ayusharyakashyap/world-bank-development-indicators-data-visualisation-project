import pandas as pd

df = pd.read_csv('health_income_wise.csv')

print("Column Names:\n", df.columns)
avg_values = df.groupby('country')[['access_to_electricity%', 'individuals_using_internet%']].mean().reset_index()
avg_values.to_csv('incomeavgwise.csv', index=False)