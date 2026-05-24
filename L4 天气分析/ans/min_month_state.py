# 请编写一个程序，读取名为 "climate_data_2017.csv" 的气象数据文件。
# 文件每一行包含一个日期（格式如 "2017-01-01"）、省份、和降雨量等信息（降雨量在第7列，下标为6）。
# 要求：统计每个月、每个省份的单日最小降雨量，并找到单日最低降雨量最大的一对（月，省份）。
# 最后，打印出这对（月，省份）的月份和省份名称。

min_mth_rain = {}

with open("climate_data_2017.csv") as f:
    next(f)
    for row in f:
        values = row.split(",")
        month, state = values[0].split("-")[1], values[1]
        rainfall = float(values[6])
        key = (month, state)
        if key in min_mth_rain:
            min_mth_rain[key] = min(min_mth_rain[key], rainfall)
        else:
            min_mth_rain[key] = rainfall

((month, state), rainfall) = max(min_mth_rain.items(),
                                  key=lambda t: t[1])

# sort(list, key = lambda x:x[1]) 匿名函数
# max(list)

print("Month:", month)
print("State:", state)
