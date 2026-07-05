# ============================================================
# Exercise 1 — 各州平均降雨量
# Method 2: 使用 pandas 的 groupby 实现
# ============================================================
# Method 1 用了 ~15 行：open → split → 字典收集 → 手动算平均
# Method 2 只需要 ~5 行：read_csv → groupby → mean → 输出
# 结果完全一样——pandas 帮你把循环和字典的活全干了。
# ============================================================

import pandas as pd

# 读取数据——pandas 自动处理标题行、逗号分隔、类型转换
df = pd.read_csv("climate_data_2017.csv")

# groupby('state') → 按州分组
# ['rainfall'].mean() → 对每个州的 rainfall 求平均值
# 返回一个 Series，索引是州名，值是平均降雨量
avg_rain = df.groupby('state')['rainfall'].mean()

# 按州名字母顺序输出
for state in sorted(avg_rain.index):
    print(state, ":", round(float(avg_rain[state]), 1))

# 💡 对比 Method 1：
# Method 1 的 rain_by_state[state].append(rainfall) → 就是 groupby 在做的事
# Method 1 的 sum(list)/len(list) → 就是 .mean() 在做的事
# 理解了 Method 1，再用 Method 2 才不是"黑盒调用"

'''output
NSW : 2.1
QLD : 5.1
SA : 2.8
TAS : 2.5
VIC : 2.7
WA : 7.8
'''
