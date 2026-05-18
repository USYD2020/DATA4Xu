# 问题说明：
# 给定一个名为 "climate_data_Dec2017.csv" 的气象数据文件，
# 每一行为一天的气象信息（首行为标题），其中第1列为日期（如"2017-12-01"），
# 第13列（下标为12）为当天上午6点的相对湿度值。
# 请你编写代码，统计有多少天上午6点湿度超过80，并打印出结果。
# 具体要求是：只统计每一天一次，当某天的6am湿度值大于80，则认为这一天计入统计；最后输出符合条件的天数。


humid_days = {}
is_first_line = True

for row in open("climate_data_2017.csv"):
    if is_first_line:
        is_first_line = False
    else:
        values = row.split(",")
        date = values[0]
        humidity = float(values[12])
        if humidity > 80:
            if date not in humid_days:
                humid_days[date] = 1

print("There were", len(humid_days), "days with humidity greater than 80")
