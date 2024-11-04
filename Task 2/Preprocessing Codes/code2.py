import pandas as pd

df = pd.read_csv('world_bank_development_indicators.csv')
df['date'] = pd.to_datetime(df['date'], format='%d-%m-%Y')

df_1970 = df[df['date'].dt.year == 1970][['country', 'rural_population', 'population', 'birth_rate']]

df_1970['rural_population_percentage'] = (df_1970['rural_population'] / df_1970['population']) * 100
df_1970_clean = df_1970.dropna(subset=['rural_population_percentage', 'birth_rate'])


df_1970_clean = df_1970_clean[['country', 'rural_population_percentage', 'birth_rate']]'
df_1970_clean.to_csv('finalbirth.csv', index=False)