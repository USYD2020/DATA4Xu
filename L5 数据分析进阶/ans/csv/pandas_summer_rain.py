# ============================================================
# 问题：找出2017年所有最高温超过35°C的"高温天"中，
#       降雨量最大的是多少毫米？
# ============================================================

import pandas as pd

# 读取整年的气候数据 dataframe

df = pd.read_csv('climate_data_2017.csv')

# 创建一个布尔Series（True/False的列表）
# 每一行：如果最高温 > 35，就是 True，否则 False
is_hot_day = df['Maximum temperature (C)'] > 35
# [0,1,1,1,0...,0,0,0,0,0]``

# 用布尔索引筛选：只保留 is_hot_day 为 True 的行
# 这就是 pandas 最强大的功能之一 —— 布尔筛选（Boolean Indexing）
hot_days = df[is_hot_day]

# 从筛选后的数据中，取出 "Rainfall (mm)" 列，求最大值
max_rain = hot_days['Rainfall (mm)'].max()

# 一行代码写法如下：
# max_rain = df[df['Maximum temperature (C)'] > 35]]['Rainfall (mm)'].max()

# 输出结果
print('Maximum amount of rainfall on hot days:', float(max_rain), 'mm')

# 💡 知识点：
# 1. pd.read_csv() 读取CSV文件为DataFrame（二维表格）
# 2. df['列名'] > 值 → 生成布尔Series
# 3. df[布尔Series] → 筛选出True对应的行（核心技巧！）
# 4. .max() 求某列的最大值

'''output
Maximum amount of rainfall on hot days: 67.3 mm
'''