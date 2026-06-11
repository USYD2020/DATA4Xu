# ============================================================
# 问题：算出每个州上午9点温度的平均值，
#       然后从高到低排序输出。
# ============================================================

import pandas as pd

# 读取气候数据
df = pd.read_csv('climate_data_2017.csv')

# groupby('state')：按州分组
# ['temp9am'].mean()：对每个州的 temp9am 列求平均值
# 结果是一个 Series：索引是州名，值是平均温度
avg_temp_by_state = df.groupby('state')['temp9am'].mean()

# sort_values() 默认从小到大（ascending=True）
# 我们要从高到低，所以 ascending=False
sorted_avg_temp = avg_temp_by_state.sort_values(ascending=False)

# Series 的 .items() 和字典的 .items() 用法一样
# 每一项是 (索引, 值)，也就是 (州名, 平均温度)
for state, temp in sorted_avg_temp.items():
    print(state, ":", round(float(temp), 1))

# 💡 知识点：
# 1. groupby + .mean() → 对每组求平均值（之前学过 .max() 和 .size()）
# 2. .sort_values(ascending=False) → 按值从大到小排序
# 3. Series.items() → 像字典一样遍历 (索引, 值)

'''output
WA : 27.1
QLD : 25.0
NSW : 21.8
SA : 20.3
VIC : 16.8
TAS : 13.5
'''
