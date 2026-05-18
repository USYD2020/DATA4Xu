# 问题注释:
# 给定一个名为“climate_data_2017.csv”的CSV格式数据文件，其内容首行为表头，后续每行为一条气象观测记录。
# 文件的每一行数据包含风向（第10列，wdir），温度（第12列，temperature）和湿度（第13列，humidity），索引从0开始。
# 请你编写程序，将所有记录依照“风向(wdir)”和“湿度(humidity)分箱(每20为一箱)”进行分组，
# 对每个分组中的“温度(temperature)”取平均值，并输出每个分组的键(key)（风向和湿度箱的元组）和对应的平均温度（保留小数点后一位）。

temperatures = {}
is_first_line = True

for row in open("climate_data_2017.csv"):
    if is_first_line:
        is_first_line = False
    else:
        values = row.split(",")
        wdir = values[9]
        humidity = float(values[12])
        temperature = float(values[11])

        humidity_bin = humidity // 20

        dict_key = (wdir, humidity_bin)
        if dict_key not in temperatures:
            temperatures[dict_key] = [temperature]
        else:
            temperatures[dict_key].append(temperature)

for key in sorted(temperatures):
    temps = temperatures[key]
    print(key, ":", round(sum(temps)/len(temps), 1))
