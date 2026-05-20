humidays = {}
is_first_line = True

for row in open('climate_data_2017(1).csv'):
    if is_first_line:
        is_first_line = False
        continue

    values = row.split(',')
    date = values[1]
    humidity = float(values[12])
    if humidity > 80:
        humidays[date] = humidity
    if date in humidays:
        continue
print(f'There were {len(humidays)} days with humidity greater than 80')