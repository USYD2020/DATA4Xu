# L2 数据分析练习题集

## 练习 1: COMP 课程成绩分析 ⭐⭐

现在你有一个成绩文件 `comp_grades.txt`，每一行都长这样：`学生名,课程编号,分数`。

你的任务是写一个小程序，把这个文件里的数据读进来，先按课程整理分数，再只筛选出 `COMP` 开头的课程，最后算出这些课程的平均分。

这道题的重点不是高级算法，而是先想清楚：

1. 原始数据长什么样
2. 你想把它存成什么字典
3. 你要怎么筛选出自己真正关心的数据

**要求：**

1. 用 `input('enter filename: ')` 读取文件名, 如果用户没有输入文件名，则使用默认文件名'comp_grades.txt'
2. 跳过第一行表头
3. 用 `split(',')` 拆出每行里的课程和分数
4. 用字典把同一门课的所有分数存到同一个列表里
5. 只统计课程编号以 `COMP` 开头的课程
6. 计算每门 `COMP` 课程的平均分，并保留两位小数输出
7. 先打印完整的 `grades dictionary:`，再打印 `COMP course averages:`
8. 如果文件不存在，输出 `no such filename`

### 思路提醒

- 这题其实是在做最基础的数据分析流程：**读数据 → 整理数据 → 筛选数据 → 统计结果**
- 这里的字典可以设计成这样：

```python
{
    'COMP1010': [85.0, 72.0],
    'COMP1020': [90.0, 66.0]
}
```

也就是说：**key 是课程编号，value 是这门课所有学生的分数列表**。

### 常见易错点

- 忘记跳过表头，导致 `score` 那一列没法转成 `float`
- 忘记对分数做 `strip()`，导致换行符还留在字符串里
- 在 `grades[course].append(score)` 之前，没有先判断这门课是不是第一次出现
- 把“按课程分组”和“筛选 COMP 课程”写混了，建议先分组，再筛选
- 平均分不是直接打印总分，而是 `总分 / 人数`

### 测试代码 + 预期输出

假设输入文件是 `comp_grades.txt`，内容如下：

```python
student,course,score
Alice,COMP1010,85
Alice,MATH1001,78
Bob,COMP1010,72
Bob,COMP1020,90
Cathy,INFO1110,88
David,COMP1020,66
Emma,COMP2010,91
Frank,ENGG1000,74
```

程序运行示例：

```python
enter filename: comp_grades.txt
grades dictionary:
{'COMP1010': [85.0, 72.0], 'MATH1001': [78.0], 'COMP1020': [90.0, 66.0], 'INFO1110': [88.0], 'COMP2010': [91.0], 'ENGG1000': [74.0]}

COMP course averages:
COMP1010  78.50
COMP1020  78.00
COMP2010  91.00
```

如果文件不存在：

```python
enter filename: wrong.txt
no such filename
```

### 代码框架

```python
print('第一步：先看成绩文件的每一行长什么样。')
print('第二步：再看字典是怎样把同一门课的分数放在一起的。')
print('第三步：最后看怎样筛选 COMP 课程并计算平均分。')
print()

filename = input('enter filename: ')
first_line = True
grades = {}

try:
    file = open(filename, 'r')
    lines = file.readlines()

    for line in lines:
        if first_line:
            first_line = False
            continue

        # 按逗号拆出课程和分数
        # score 要转成 float
        pass

        # 如果这门课第一次出现，先创建空列表
        pass

        # 把分数加进这门课对应的列表
        pass

    file.close()

    comp_stats = {}

    # 遍历 grades，只处理 COMP 开头的课程
    # 算出平均分后存到 comp_stats
    pass

    print('grades dictionary:')
    print(grades)
    print()
    print('COMP course averages:')

    # 按格式输出每门课的平均分
    pass

except FileNotFoundError:
    print('no such filename')
```

### 加一点思考

如果以后你不只想统计 `COMP`，而是想统计 `MATH`、`INFO` 或别的课程，其实你只需要改“筛选条件”那一小部分。这就是为什么先把数据整理成字典，会比一边读文件一边乱算更清楚。
