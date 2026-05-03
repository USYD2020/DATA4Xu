print('第一步：先看 comp_grades.txt 的每一行长什么样。')
print('第二步：再看字典 grades 是怎样把一个学生的多门课存起来的。')
print('第三步：最后看 course.startswith("COMP") 是怎样筛选课程并计算平均分的。')
print()

filename = input('enter filename: ')
# 如果用户没有输入文件名，则使用默认文件名
if not filename:
    filename = 'comp_grades.txt'

# 用来跳过第一行表头
first_line = True

# 这个字典用来存储每个学生和他们各门课程的分数
# 结构类似于: {
#   '张三': {'COMP1010': 95.0, 'MATH1010': 88.0},
#   '李四': {'COMP1020': 89.5}
# }
grades = {}

try:
    # 打开文件并读取所有行
    file = open(filename, 'r')
    lines = file.readlines()

    # 遍历每一行，跳过第一行表头
    for line in lines:
        if first_line:
            first_line = False
            continue

        # 按逗号分开每一列：学生，课程，分数
        _, course, score = line.split(',')
        course = course    # 课程名字
        score = float(score.strip())  # 分数（变成float类型）

        if course not in grades:
            grades[course] = []

        # 在字典中，存下这门课的分数
        grades[course].append(score)

    file.close()

    # 创建一个新字典用于统计COMP课程的总分和人数
    # 结构类似于：{'COMP101': {'total': 288, 'count': 3}}
    comp_stats = {}

    # 遍历每个学生和他们所有的课程
    for course in grades:
        # 只统计课程名以'COMP'开头的课
        if course.startswith('COMP'):
            total_score = sum(grades[course])
            total_count = len(grades[course])
            comp_stats[course] = total_score / (total_count * 1.0)

    print('grades dictionary:')
    print(grades)  # 打印完整的分数字典
    print()
    print('COMP course averages:')

    # 计算每门COMP课程的平均分并输出
    for course in comp_stats:
        average = comp_stats[course]
        print(f'{course:10s}{average:.1f}')

except FileNotFoundError:
    print('no such filename')
