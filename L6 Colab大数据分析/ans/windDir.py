import pandas as pd
df = pd.read_csv('./test/climate_data_2017.csv')

all_wind_dirs = sorted(df['wind_dir']. unique ())

# # extract year from date value
# df["year"] = df['date'].apply(lambda x: x.split('-')[0])

# Filter for rows in 2017 and group by 'wind_dir'
grouped_data_2017 = df[df['date'].str.startswith('2017')].groupby('wind_dir')
wind_dir_counts = grouped_data_2017.size()

# Iterate through all possible wind directions and print counts
for d in all_wind_dirs:
    value = wind_dir_counts.get(d, 0)
    print(f"{d} : {value}")