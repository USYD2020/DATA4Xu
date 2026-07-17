# ============================================================
# Exercise 1 — 各课程平均总评成绩
# Method 1: 使用 Python 原生方法 with open 读取
# ============================================================
# open → 跳标题 → split → 计算 final_mark → 字典收集 → 手动统计
# 这是理解 pandas 新列计算和 groupby().mean() 的基础。
# ============================================================

final_marks_by_course = {}

with open("student_assessment_results.csv") as f:
    next(f)  # 跳过标题行
    for row in f:
        values = row.strip().split(",")

        course = values[3]               # 第 4 列：课程编号
        assignment = float(values[5])    # 第 6 列：作业分
        exam = float(values[6])          # 第 7 列：考试分

        # 总评成绩 = 作业分 + 考试分
        final_mark = assignment + exam

        # 如果这门课第一次出现，先创建空列表
        if course not in final_marks_by_course:
            final_marks_by_course[course] = []

        # 把这条记录的总评成绩追加进去
        final_marks_by_course[course].append(final_mark)

# 按课程编号字母顺序遍历，计算平均值
for course in sorted(final_marks_by_course):
    mark_list = final_marks_by_course[course]
    avg = sum(mark_list) / len(mark_list)
    print(course, ":", round(avg, 1))

# 💡 知识点：
# 1. with open() as f → 安全打开文件，结束后自动关闭
# 2. next(f) → 跳过第一行标题
# 3. strip() + split(",") → 去掉换行 + 按逗号拆字段
# 4. final_mark = assignment + exam → 手动计算新字段
# 5. 字典 key=课程编号, value=总评成绩列表 → 收集同一门课的数据

'''output
COMM1190 : 73.6
COMM2501 : 75.0
COMP1010 : 65.1
COMP2123 : 72.0
DATA1001 : 71.9
DATA2001 : 78.3
'''
