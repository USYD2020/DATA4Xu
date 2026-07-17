# ============================================================
# Exercise 2 — 学习风险指数排名
# 风险由测试通过率、花费时间、深夜提交三个因素合成
# ============================================================

import pandas as pd

# 读取 Python 学习日志数据
df = pd.read_csv("python_learning_log.csv")

# 1. 计算测试通过率
# 通过率越低，后面的风险分越高
df["pass_rate"] = df["tests_passed"] / df["tests_total"]

# 2. 判断是否深夜提交
# 晚上 9 点之后（>=21）或凌晨 2 点之前（<=2）算深夜提交
# apply(lambda h: ...) 表示对 submission_hour 这一列的每个值 h 都执行一次判断
df["late_submission"] = df["submission_hour"].apply(
    lambda h: 1 if h >= 21 or h <= 2 else 0
)

# 3. 计算学习风险指数
# 三部分：未通过比例、花费时间、深夜提交
df["risk_score"] = (
    (1 - df["pass_rate"]) * 60
    + (df["minutes_spent"] / 80) * 25
    + df["late_submission"] * 15
)

# 4. 对每个学生，计算平均风险指数
avg_risk_by_student = df.groupby("student_id")["risk_score"].mean()

# 5. 按风险指数从高到低排序
sorted_risk = avg_risk_by_student.sort_values(ascending=False)

# 6. 输出结果
for student_id, score in sorted_risk.items():
    print(student_id, ":", round(float(score), 1))

# 💡 知识点：
# 1. 特征工程：从原始列构造 pass_rate、late_submission、risk_score
# 2. apply(lambda h: ...) → 对一整列逐个应用判断逻辑
# 3. 一个公式里组合多个列，是数据分析中很常见的做法
# 4. groupby().mean() → 对每个学生聚合多周记录
# 5. sort_values(ascending=False) → 从高风险到低风险排序

'''output
z5400004 : 65.0
z5400002 : 49.5
z5400005 : 19.0
z5400001 : 15.6
z5400003 : 8.2
'''
