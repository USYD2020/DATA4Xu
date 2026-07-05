# ============================================================
# Exercise 2 — 各州高湿天的统计
# 筛选 humidity9am > 80 的记录，按州统计天数和平均温度
# ============================================================

import pandas as pd

# 读取数据
df = pd.read_csv("climate_data_2017.csv")

# 获取所有州名（排好序），用于最终输出——保证不遗漏
all_states = sorted(df['state'].unique())

# 布尔筛选：只保留 humidity9am > 80 的行
# 这就是 L5/L6 学过的核心技巧——先缩小范围，再做统计
humid_days = df[df['humidity9am'] > 80]

# 对筛选后的数据按州分组，统计条数（天数）
# .size() 返回每组的行数，和 L6 的风向计数一样
count_dict = humid_days.groupby('state').size().to_dict()

# 对筛选后的数据按州分组，算 temp9am 的平均值
temp_dict = humid_days.groupby('state')['temp9am'].mean().to_dict()

# 遍历所有州名
# 注意：SA 和 WA 没有高湿记录，不会出现在 count_dict 里
# 所以要用 .get(state, 0) 来兜底——取不到就返回 0
for state in all_states:
    count = count_dict.get(state, 0)
    if count > 0:
        avg_temp = round(temp_dict[state], 1)
        print(f"{state} : {count} days, avg temp {avg_temp}")
    else:
        print(f"{state} : 0 days, avg temp N/A")

# 💡 知识点：
# 1. 布尔筛选 df[df['列'] > 值] → 缩小范围后再分组
# 2. 同一个筛选结果可以做多种聚合（.size() 和 .mean()）
# 3. .get(key, default) → 字典里取不到就返回默认值
# 4. 真实数据分析常见场景：不是所有分组都有数据，要处理缺失

'''output
NSW : 4 days, avg temp 21.0
QLD : 3 days, avg temp 25.9
SA : 0 days, avg temp N/A
TAS : 6 days, avg temp 13.0
VIC : 2 days, avg temp 15.9
WA : 0 days, avg temp N/A
'''
