# ============================================================
# Exercise 1 — 各课程平均总评成绩
# Method 2: Use package，用 pandas 的 groupby 实现
# ============================================================
# Method 1 手动计算每一行的 final_mark，再用字典分组。
# Method 2 用 pandas 直接整列相加，再 groupby 求平均。
# ============================================================

import pandas as pd

# 读取数据
# pandas 会自动识别第一行为标题行
df = pd.read_csv("student_assessment_results.csv")

# 创建新列：总评成绩 = 作业分 + 考试分
# pandas 可以直接对整列做加法，不需要手动写 for 循环
df["final_mark"] = df["assignment"] + df["exam"]

# 按课程编号分组，对 final_mark 求平均值
avg_final = df.groupby("course")["final_mark"].mean()

# 按课程编号字母顺序输出
for course in sorted(avg_final.index):
    print(course, ":", round(float(avg_final[course]), 1))

# 💡 对比 Method 1：
# Method 1 的 final_mark = assignment + exam → pandas 用整列相加完成
# Method 1 的 final_marks_by_course[course].append(final_mark) → groupby 在做
# Method 1 的 sum(list)/len(list) → .mean() 在做

'''output
COMM1190 : 73.6
COMM2501 : 75.0
COMP1010 : 65.1
COMP2123 : 72.0
DATA1001 : 71.9
DATA2001 : 78.3
'''
