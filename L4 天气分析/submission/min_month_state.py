min_mth_rain = {}
is_first_line = True

for row in open('climate_data_2017(1).csv'):
    if is_first_line:
        is_first_line = False
        continue

    values = row.split(',')
    month = values[0].split('-')[1]
    state = values[1]
    rainfall = float(values[6])
    key = (month,state)
    if key in min_mth_rain:
        min_mth_rain[key] = min(rainfall,min_mth_rain[key])
    else:
        min_mth_rain[key] = rainfall

key_min = ()
max_rainfall = -1
for i,r in min_mth_rain.items():
    if r > max_rainfall:
        max_rainfall = r
        key_min = i
        # print("update", i,r)
print('Month:', key_min[0])
print('State:', key_min[1])