import pandas as pd

df = pd.read_csv("climate_data_2017.csv")

# 按 State 分组
grouped_by_state = df.groupby("state")

# 对每个州，取 9am relative humidity (%) 的最大值
max_humidity_by_state = grouped_by_state["humidity9am"].max()

# 可以转成字典，再按 key 排序输出
max_humidity_by_state_as_dict = max_humidity_by_state.to_dict()

for k in sorted(max_humidity_by_state_as_dict):
    print(k, ":", float(max_humidity_by_state_as_dict[k]))
