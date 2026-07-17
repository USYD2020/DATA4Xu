# ============================================================
# Exercise 1 — 各 Python 主题平均测试通过率
# Method 2: Use package，用 pandas 的 groupby 实现
# ============================================================
# Method 1 手动计算每一行的 pass_rate，再用字典分组。
# Method 2 用 pandas 直接整列相除，再 groupby 求平均。
# ============================================================

import pandas as pd

# 读取数据
# pandas 会自动识别第一行为标题行
df = pd.read_csv("python_learning_log.csv")

# 创建新列：测试通过率 = 通过测试数 / 总测试数
# pandas 可以直接对整列做除法，不需要手动写 for 循环
df["pass_rate"] = df["tests_passed"] / df["tests_total"]

# 按 topic 分组，对 pass_rate 求平均值
avg_pass_rate = df.groupby("topic")["pass_rate"].mean()

# 按 topic 字母顺序输出
for topic in sorted(avg_pass_rate.index):
    print(topic, ":", round(float(avg_pass_rate[topic]) * 100, 1), "%")

# 💡 对比 Method 1：
# Method 1 的 pass_rate = tests_passed / tests_total → pandas 用整列相除完成
# Method 1 的 pass_rates_by_topic[topic].append(pass_rate) → groupby 在做
# Method 1 的 sum(list)/len(list) → .mean() 在做

'''output
dictionaries : 76.7 %
file_io : 77.5 %
functions : 76.0 %
lists : 80.0 %
loops : 77.5 %
pandas_groupby : 70.0 %
pandas_intro : 76.0 %
variables : 88.0 %
'''
