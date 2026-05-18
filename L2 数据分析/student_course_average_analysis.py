print('第一步：先看 retake_grades.txt 的每一行长什么样。')  # Step 1: examine the lines in the file
print('第二步：再想想怎样把同一个学生的同一门课多次成绩存起来。')  # Step 2: consider how to store multiple grades per student per course
print('第三步：最后计算每个学生每门课的平均分。')  # Step 3: calculate the averages
print()

filename = input('enter filename: ')
if not filename:
    filename = 'retake_grades.txt'   # Default file name if no input

first_line = True    # Skip the header line
grades = {}          # Dictionary to store grades

try:
    file = open(filename, 'r')
    lines = file.readlines()
except FileNotFoundError:
    print('no such filename')
    
for line in lines:
    if first_line:
        first_line = False      # Skip the first line (header)
        continue

    student, course, score = line.split(',')     # Split line into fields
    student = student.strip()
    course = course.strip()
    score = float(score.strip())

    # Create nested dictionaries/lists as needed
    if student not in grades:
        grades[student] = {}

    if course not in grades[student]:
        grades[student][course] = []

    grades[student][course].append(score)      # Append the score




print('grades dictionary:')
print(grades)
print()
print('student course averages:')

# Compute and output each student's average for each course
for student in grades:
    for course in grades[student]:
        attempts = grades[student][course]
        average = sum(attempts) / len(attempts)

        if len(attempts) == 1:
            print(f'{student:10s}{course:10s}{average:.1f} Only')   # Show if only one attempt
        else:
            print(f'{student:10s}{course:10s}{average:.1f}')


