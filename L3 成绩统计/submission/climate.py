temperature = {}
is_first_line = True
for row in open('climate_data_2017.csv'):
    if is_first_line:
        is_first_line = False
        continue

    values = row.split(',')
    wdir, temp, humidity = values[-4], values[-2], values[-1]
    temp = float(temp)
    humidity = float(humidity)
    humidity_bin = humidity // 20

    # key只能用元组，元组的语法是用括号表示
    key = (wdir, humidity_bin)
    # 当 key 首次存在时，注意初始化，initialize as empty list
    if key not in temperature:
        temperature[key] = []
    # 注意这里没有 else，也就是每次都会更新 新的 temp 进入 key 所对的列表
    temperature[key].append(temp)

# 注意用 sorted 函数来按自然顺序排序
for i in sorted(temperature.keys()):
    average = sum(temperature[i]) / len(temperature[i])
    print("{} : {:.1f}".format(i, average))
