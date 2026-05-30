import pandas as pd

df = pd.read_csv("climate_data_2017(1).csv")

# 先做一个 True/False 条件：哪些行是高温天
is_hot_day = df["temp9am"] > 35.0

# 用上面的条件筛选出高温天
hot_days = df[is_hot_day]

# 在高温天里找 Rainfall (mm) 的最大值
max_rain = hot_days["rainfall"].max()

print("Maximum amount of rainfall on hot days:", float(max_rain), "mm")
