# ============================================================
# Exercise 2 — 各学院风险学生统计
# 风险条件：final_mark < 60 或 attendance < 70
# ============================================================

import pandas as pd

# 读取数据
df = pd.read_csv("student_assessment_results.csv")

# 创建总评成绩新列
df["final_mark"] = df["assignment"] + df["exam"]

# 获取所有学院名（排好序），保证最终输出不遗漏学院
all_faculties = sorted(df["faculty"].unique())

# 布尔筛选：总评低于 60，或者出勤率低于 70
# 注意：多个 pandas 条件要分别加括号
# | 表示“或者”，& 表示“并且”
risk_records = df[(df["final_mark"] < 60) | (df["attendance"] < 70)]

# 对风险记录按学院分组，统计记录数
count_dict = risk_records.groupby("faculty").size().to_dict()

# 对风险记录按学院分组，计算平均总评成绩
avg_final_dict = risk_records.groupby("faculty")["final_mark"].mean().to_dict()

# 遍历所有学院名
# 如果某学院没有风险记录，.get(faculty, 0) 会返回 0
for faculty in all_faculties:
    count = count_dict.get(faculty, 0)
    if count > 0:
        avg_final = round(avg_final_dict[faculty], 1)
        print(f"{faculty} : {count} students, avg final {avg_final}")
    else:
        print(f"{faculty} : 0 students, avg final N/A")

# 💡 知识点：
# 1. df["assignment"] + df["exam"] → 整列相加，创建新列
# 2. (条件1) | (条件2) → pandas 的“或者”筛选
# 3. df[条件] → 只保留符合条件的行
# 4. groupby().size() → 每组记录数
# 5. groupby()["final_mark"].mean() → 每组平均总评成绩

'''output
Business : 2 students, avg final 49.0
Engineering : 3 students, avg final 49.3
Science : 3 students, avg final 54.7
'''
