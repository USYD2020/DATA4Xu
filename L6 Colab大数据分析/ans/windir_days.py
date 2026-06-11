import pandas as pd

df = pd.read_csv("Climate_data_2017.csv")
all_wind_dirs = sorted(df['wind_dir'].dropna().unique())
grouped_data_2017 = df[df['date'].str.startswith('2017')].groupby('wind_dir')
wind_dir_counts = grouped_data_2017.size()

for d in all_wind_dirs:
    value = wind_dir_counts.get(d, 0)
    print(f"{d} : {value}")
