# ============================================================
# Exercise 1 — 各课程平均成绩
# Method 2: Use package，用 pandas 的 groupby 实现
# ============================================================
# Method 1 需要手动 open、split、用字典分组、再算平均。
# Method 2 用 pandas：read_csv → groupby → mean。
# ============================================================

import pandas as pd

# 读取数据——pandas 自动处理标题行、逗号分隔、类型转换
df = pd.read_csv("student_course_results.csv")

# groupby('course')：按课程编号分组
# ['mark'].mean()：对每门课的 mark 求平均值
avg_mark = df.groupby('course')['mark'].mean()

# 按课程编号字母顺序输出
for course in sorted(avg_mark.index):
    print(course, ":", round(float(avg_mark[course]), 1))

# 💡 对比 Method 1：
# Method 1 的 marks_by_course[course].append(mark) → 就是 groupby 在做的事
# Method 1 的 sum(list)/len(list) → 就是 .mean() 在做的事
# 理解了 Method 1，再用 Method 2 才不是“黑盒调用”

'''output
COMM1190 : 72.6
COMM2501 : 74.8
COMP1010 : 65.3
DATA1001 : 70.8
'''
