# ============================================================
# Exercise 2 — 各学院高表现学生统计
# 条件：mark >= 85 且 attendance >= 90
# ============================================================

import pandas as pd

# 读取数据
df = pd.read_csv("student_course_results.csv")

# 获取所有学院名（排好序），保证最终输出不遗漏学院
all_faculties = sorted(df['faculty'].unique())

# 布尔筛选：成绩 >= 85 且出勤率 >= 90
# 注意：多个 pandas 条件要分别加括号，中间用 & 连接
high_records = df[(df['mark'] >= 85) & (df['attendance'] >= 90)]

# 对筛选后的数据按学院分组，统计记录数
count_dict = high_records.groupby('faculty').size().to_dict()

# 对筛选后的数据按学院分组，计算平均成绩
avg_mark_dict = high_records.groupby('faculty')['mark'].mean().to_dict()

# 遍历所有学院名
# 如果某学院没有高表现记录，.get(faculty, 0) 会返回 0
for faculty in all_faculties:
    count = count_dict.get(faculty, 0)
    if count > 0:
        avg_mark = round(avg_mark_dict[faculty], 1)
        print(f"{faculty} : {count} students, avg mark {avg_mark}")
    else:
        print(f"{faculty} : 0 students, avg mark N/A")

# 💡 知识点：
# 1. (条件1) & (条件2) → pandas 多条件筛选
# 2. df[条件] → 只保留符合条件的行
# 3. groupby().size() → 每组记录数
# 4. groupby()['mark'].mean() → 每组平均成绩
# 5. dict.get(key, default) → 处理某组没有数据的情况

'''output
Business : 4 students, avg mark 90.2
Engineering : 1 students, avg mark 94.0
Science : 2 students, avg mark 89.0
'''
