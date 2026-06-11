# ============================================================
# 问题：对每个州，找出2017年总降雨量最大的月份，
#       输出州名、月份和那个月的总降雨量。
# ============================================================

import pandas as pd

# 读取气候数据
df = pd.read_csv('climate_data_2017.csv')

# 从 date 列提取月份
# '2017-01-03'.split('-') → ['2017', '01', '03']，取下标 1 就是月份
# .str 让我们对一整列字符串做同样的操作，不用自己写循环
df['month'] = df['date'].str.split('-').str[1]

# groupby 可以传一个列表，按多列分组
# 分组的 key 会变成元组：('NSW', '01')、('NSW', '02')...
# 对每组的 rainfall 求和
rain_by_state_month = df.groupby(['state', 'month'])['rainfall'].sum()

# 转成字典，key 是 (state, month) 元组，value 是总降雨量
rain_dict = rain_by_state_month.to_dict()

# 对每个州，找出总降雨量最大的月份
# 这一步和 L4 用 (month, state) 当 key 找最值的套路一样
best = {}
for (state, month), total in rain_dict.items():
    if state not in best or total > best[state][1]:
        best[state] = (month, total)

# 按州名字母顺序输出
for state in sorted(best):
    month, total = best[state]
    print(state, ":", month, ":", round(float(total), 1))

# 💡 知识点：
# 1. df['列'].str.split('-').str[1] → 对整列字符串拆分取段
# 2. groupby(['列1', '列2']) → 多列分组，key 是元组
# 3. .sum() → 对每组求和
# 4. pandas 算完之后，"组内找最大"还是回到字典遍历的老套路

'''output
NSW : 05 : 4.4
QLD : 02 : 13.5
SA : 04 : 6.0
TAS : 01 : 5.6
VIC : 06 : 6.2
WA : 02 : 16.2
'''
