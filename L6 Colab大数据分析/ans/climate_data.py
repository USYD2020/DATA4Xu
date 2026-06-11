import pandas as pd
df = pd.read_csv('Climate_data_2017.csv')
is_hot_days = df[df['Maximum temperature (C)'] > 35]
max_rain = is_hot_days['Rainfall (mm)'].max()
print(max_rain)