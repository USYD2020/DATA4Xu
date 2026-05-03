# L2 数据分析练习题集

## 练习 2: 补考成绩平均分分析 ⭐⭐⭐

现在题目变难一点了。

同一个学生的同一门课，可能会考不止一次。比如第一次 fail 了，后来又补考了一次。你的任务是把这些数据读进来，然后输出**每个学生每门课的平均分**。

如果某个学生某门课只考过一次，就在这个分数后面加上 `Only`。
如果考过多次，就只输出平均分，不要加标签。

这道题的关键是：你不能再只按“课程”分组了，因为现在你需要同时记住：
1. 是哪个学生
2. 是哪门课
3. 这门课考了几次
4. 每次分别多少分

**要求：**

1. 用 `input('enter filename: ')` 读取文件名
2. 如果用户直接回车，就默认使用 `retake_grades.txt`
3. 跳过第一行表头
4. 用 `split(',')` 拆出学生名、课程编号和分数
5. 用合适的数据结构存下“每个学生每门课的所有分数”
6. 计算每个学生每门课的平均分
7. 如果这门课只考过一次，输出时在分数后面加 `Only`
8. 如果考过多次，只输出平均分
9. 先打印完整的 `grades dictionary:`，再打印 `student course averages:`
10. 如果文件不存在，输出 `no such filename`

### 测试代码 + 预期输出

假设输入文件 `retake_grades.txt` 内容如下：

```python
student,course,score
Alice,COMP1010,45
Alice,COMP1010,85
Alice,MATH1001,78
Bob,COMP1010,72
Bob,COMP1020,40
Bob,COMP1020,90
Cathy,INFO1110,88
David,COMP1020,66
Emma,COMP2010,49
Emma,COMP2010,91
Frank,ENGG1000,74
```

程序运行示例：

```python
enter filename: retake_grades.txt
grades dictionary:
{'Alice': {'COMP1010': [45.0, 85.0], 'MATH1001': [78.0]}, 'Bob': {'COMP1010': [72.0], 'COMP1020': [40.0, 90.0]}, 'Cathy': {'INFO1110': [88.0]}, 'David': {'COMP1020': [66.0]}, 'Emma': {'COMP2010': [49.0, 91.0]}, 'Frank': {'ENGG1000': [74.0]}}

student course averages:
Alice     COMP1010  65.0
Alice     MATH1001  78.0 Only
Bob       COMP1010  72.0 Only
Bob       COMP1020  65.0
Cathy     INFO1110  88.0 Only
David     COMP1020  66.0 Only
Emma      COMP2010  70.0
Frank     ENGG1000  74.0 Only
```

如果文件不存在：

```python
enter filename: wrong.txt
no such filename
```

### 代码框架

```python
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

        # 拆出 student, course, score
        # score 转成 float
        pass

        # 如果 student 第一次出现，先建一个空字典
        pass

        # 如果这门课第一次出现在这个学生名下，先建空列表
        pass

        # 把这次成绩加进列表里
        pass

    file.close()

    print('grades dictionary:')
    print(grades)
    print()
    print('student course averages:')

    # 遍历每个学生、每门课
    # 计算平均分
    # 如果只有一次成绩，就在后面加 Only
    pass

except FileNotFoundError:
    print('no such filename')
```

### 这题比上一题难在哪

上一题只需要按课程分组，这一题要按“学生 + 课程”两层来分组，所以更适合用嵌套字典。

你可以把它想成这样：

```python
{
    'Alice': {
        'COMP1010': [45.0, 85.0],
        'MATH1001': [78.0]
    },
    'Bob': {
        'COMP1020': [40.0, 90.0]
    }
}
```

这样一来，你既能知道是谁，也能知道他哪门课考了几次。

### 易错点提醒

- 忘记先初始化 `grades[student]`
- 忘记先初始化 `grades[student][course]`
- 把分数直接覆盖掉，导致补考记录丢失
- 平均分应该是 `sum(list) / len(list)`
- `Only` 只在这门课只有一次成绩时才加
