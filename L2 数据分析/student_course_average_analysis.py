print('第一步：先看 retake_grades.txt 的每一行长什么样。')
print('第二步：再想想怎样把同一个学生的同一门课多次成绩存起来。')
print('第三步：最后计算每个学生每门课的平均分。')
print()

filename = input('enter filename: ')
if not filename:
    filename = 'retake_grades.txt'

first_line = True
grades = {}

try:
    file = open(filename, 'r')
    lines = file.readlines()

    for line in lines:
        if first_line:
            first_line = False
            continue

        student, course, score = line.split(',')
        student = student.strip()
        course = course.strip()
        score = float(score.strip())

        if student not in grades:
            grades[student] = {}

        if course not in grades[student]:
            grades[student][course] = []

        grades[student][course].append(score)

    file.close()

    print('grades dictionary:')
    print(grades)
    print()
    print('student course averages:')

    for student in grades:
        for course in grades[student]:
            attempts = grades[student][course]
            average = sum(attempts) / len(attempts)

            if len(attempts) == 1:
                print(f'{student:10s}{course:10s}{average:.1f} Only')
            else:
                print(f'{student:10s}{course:10s}{average:.1f}')

except FileNotFoundError:
    print('no such filename')
