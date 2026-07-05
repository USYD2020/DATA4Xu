# ============================================================
# Exercise 1 — 各课程平均成绩
# Method 1: 使用 Python 原生方法 with open 读取
# ============================================================
# open → 跳标题 → split → 字典收集 → 手动统计
# 这是理解 pandas groupby().mean() 的基础。
# ============================================================

marks_by_course = {}

with open("student_course_results.csv") as f:
    next(f)  # 跳过标题行
    for row in f:
        values = row.strip().split(",")

        course = values[3]          # 第 4 列：课程编号
        mark = float(values[5])     # 第 6 列：成绩

        # 如果这门课第一次出现，先创建空列表
        if course not in marks_by_course:
            marks_by_course[course] = []

        # 把这条记录的成绩追加进去
        marks_by_course[course].append(mark)

# 按课程编号字母顺序遍历，计算平均值
for course in sorted(marks_by_course):
    mark_list = marks_by_course[course]
    avg = sum(mark_list) / len(mark_list)
    print(course, ":", round(avg, 1))

# 💡 知识点：
# 1. with open() as f → 安全打开文件，结束后自动关闭
# 2. next(f) → 跳过第一行标题
# 3. strip() + split(",") → 去掉换行 + 按逗号拆字段
# 4. 字典 key=课程编号, value=成绩列表 → 收集同一门课的所有成绩
# 5. sum(list)/len(list) → 手动求平均

'''output
COMM1190 : 72.6
COMM2501 : 74.8
COMP1010 : 65.3
DATA1001 : 70.8
'''
