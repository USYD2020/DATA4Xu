# L10 Colab 成绩分析练习题集

这两道题继续在 **Google Colab** 上完成。操作步骤：
1. 打开 [Google Colab](https://colab.research.google.com/)
2. 新建一个 Notebook
3. 把数据文件上传到 Colab（点击左侧文件夹图标，然后上传）
4. 在代码格里写代码，运行看结果

完成后把你的 **Colab 链接** 放到 `submission` 文件夹下。

这次继续使用和 L9 类似的**学生成绩数据**，但数据稍微更接近真实课程评估：一个学生的最终成绩不是直接给出来的，而是由平时作业分和考试分相加得到。

数据文件叫 `student_assessment_results.csv`，一行代表一名学生在某门课的一次成绩记录。

数据文件有 8 列：

| 列名 | 含义 |
|---|---|
| `student_id` | 学生编号 |
| `faculty` | 学院，例如 Science、Business、Engineering |
| `program` | 专业 |
| `course` | 课程编号，例如 DATA1001、COMM1190、COMP1010 |
| `term` | 学期，例如 T1、T2、T3 |
| `assignment` | 作业分，满分 50 |
| `exam` | 考试分，满分 50 |
| `attendance` | 出勤率 |

总评成绩的计算方式是：

```python
final_mark = assignment + exam
```

---

## Exercise 1: 各课程平均总评成绩 ⭐⭐

计算每门课程的平均总评成绩，按课程编号**字母顺序**输出。

这道题要求用**两种方法**完成：

1. **Method 1: 使用 Python 原生方法 `with open` 读取**
2. **Method 2: Use package，也就是用 pandas 的简洁语法实现**

两种方法的输出必须完全一样。先用 Method 1 把基础的文件读取、标题行处理、逐行拆字段、计算新字段、字典分组理顺；再用 pandas 把同样的逻辑用简洁语法写出来。

---

### Method 1: 使用 Python 原生方法 `with open` 读取

手动处理每一行和标题行：跳过标题行，用 `split(',')` 拆字段，计算 `final_mark = assignment + exam`，再用字典收集每门课的所有总评成绩，最后手动算平均值。

**要求：**

1. 用 `with open("student_assessment_results.csv") as f` 打开文件
2. 用 `next(f)` 跳过第一行标题
3. 每一行用 `strip()` 去掉末尾换行，再用 `split(",")` 拆字段
4. 取出 `course`（第 4 列，下标 3）
5. 取出 `assignment`（第 6 列，下标 5）和 `exam`（第 7 列，下标 6）
6. 把 `assignment` 和 `exam` 转成 `float`
7. 计算 `final_mark = assignment + exam`
8. 用一个字典，key 是课程编号，value 是这门课所有总评成绩的**列表**
9. 按课程编号字母顺序输出：`课程编号 : 平均总评成绩`
10. 平均总评成绩保留 1 位小数

#### 测试代码 + 预期输出

```python
# COMM1190 : 73.6
# COMM2501 : 75.0
# COMP1010 : 65.1
# COMP2123 : 72.0
# DATA1001 : 71.9
# DATA2001 : 78.3
```

#### 代码框架

```python
final_marks_by_course = {}

with open("student_assessment_results.csv") as f:
    next(f)  # 跳过标题行
    for row in f:
        values = row.strip().split(",")

        # 取出 course、assignment、exam
        course = None
        assignment = None
        exam = None

        # 计算总评成绩
        final_mark = None

        # 如果这门课第一次出现，先创建空列表
        # 然后把 final_mark 追加进去
        pass

# 按课程编号字母顺序输出
for course in sorted(final_marks_by_course):
    mark_list = final_marks_by_course[course]
    avg = sum(mark_list) / len(mark_list)
    print(course, ":", round(avg, 1))
```

---

### Method 2: Use package，用 pandas 简洁语法实现

同样的结果，用 pandas 可以更短：`read_csv` → 创建新列 → `groupby` → `.mean()`。

**要求：**

1. 导入 `pandas as pd`
2. 用 `pd.read_csv()` 读取 `student_assessment_results.csv`
3. 新建一列 `final_mark`，值为 `assignment + exam`
4. 用 `course` 分组
5. 对 `final_mark` 求 `.mean()`
6. 按课程编号字母顺序输出：`课程编号 : 平均总评成绩`
7. 平均总评成绩保留 1 位小数

#### 测试代码 + 预期输出

```python
# COMM1190 : 73.6
# COMM2501 : 75.0
# COMP1010 : 65.1
# COMP2123 : 72.0
# DATA1001 : 71.9
# DATA2001 : 78.3
```

#### 代码框架

```python
import pandas as pd

df = pd.read_csv("student_assessment_results.csv")

# 创建总评成绩新列
df["final_mark"] = None

# 按 course 分组，对 final_mark 求平均值
avg_final = None

# 按课程编号字母顺序输出
for course in sorted(avg_final.index):
    print(course, ":", round(float(avg_final[course]), 1))
```

### 对比两种方法

| | Method 1 `with open` | Method 2 `pandas` |
|---|---|---|
| 读文件 | 手动 `open`、`next(f)` 跳标题、`split` 拆字段 | `pd.read_csv()` 一行搞定 |
| 新字段 | 自己逐行算 `assignment + exam` | `df["assignment"] + df["exam"]` 直接整列相加 |
| 分组 | 自己用字典，`if course not in dict` 判断 | `groupby('course')` |
| 求平均 | `sum(list) / len(list)` | `.mean()` |
| 排序 | `sorted(dict)` | `sorted(series.index)` |

Method 1 是为了看清楚每一行数据是怎么变成统计结果的；Method 2 是把同样的逻辑交给 pandas，用更短的代码完成。

---

## Exercise 2: 各学院风险学生统计 ⭐⭐⭐

定义：如果一条记录满足下面任意一个条件，就算一条“风险记录”：

- `final_mark < 60`
- `attendance < 70`

注意：这里的 `final_mark` 不是原始列，需要先用 `assignment + exam` 计算出来。

你需要按学院统计：

1. 每个学院有多少条风险记录
2. 这些风险记录的平均总评成绩是多少

这题综合了 pandas 的几个重要操作：创建新列、布尔筛选、多个条件、`groupby`、`.size()`、`.mean()`。

**要求：**

1. 导入 `pandas as pd`
2. 读取 `student_assessment_results.csv`
3. 新建一列 `final_mark = assignment + exam`
4. 获取数据中所有学院名，并按字母顺序排序
5. 用两个条件筛选出风险记录：`final_mark < 60` 或者 `attendance < 70`
6. 对风险记录按 `faculty` 分组，用 `.size()` 统计每个学院的风险记录数
7. 对风险记录按 `faculty` 分组，用 `.mean()` 算每个学院风险记录的平均总评成绩
8. 把两个结果都转成字典
9. 遍历所有学院名，输出：`学院 : X students, avg final Y`
10. 如果某个学院没有风险记录，输出 `0 students, avg final N/A`
11. 平均总评成绩保留 1 位小数

### 测试代码 + 预期输出

```python
# Business : 2 students, avg final 49.0
# Engineering : 3 students, avg final 49.3
# Science : 3 students, avg final 54.7
```

### 代码框架

```python
import pandas as pd

df = pd.read_csv("student_assessment_results.csv")

# 创建总评成绩新列
df["final_mark"] = None

# 获取所有学院名，排好序
all_faculties = sorted(df["faculty"].unique())

# 布尔筛选：总评 < 60 或 出勤率 < 70
risk_records = None

# 对风险记录按 faculty 分组，统计条数
count_dict = None

# 对风险记录按 faculty 分组，算平均总评成绩
avg_final_dict = None

# 遍历所有学院名，输出
for faculty in all_faculties:
    count = count_dict.get(faculty, 0)
    if count > 0:
        avg_final = round(avg_final_dict[faculty], 1)
        print(f"{faculty} : {count} students, avg final {avg_final}")
    else:
        print(f"{faculty} : 0 students, avg final N/A")
```

### 这题在练什么

1. pandas 可以直接对两列做运算：`df["assignment"] + df["exam"]`
2. 多个条件要分别加括号
3. `|` 表示“或者”，`&` 表示“并且”
4. 布尔筛选先缩小范围，再做分组统计
5. 真实成绩分析中，经常需要先定义“风险学生”的规则，再按学院、课程或学期统计

---

## 提交说明

完成后，在 `submission` 文件夹下新建一个文件（比如 `你的名字_L10.txt`），把你的 Colab Notebook 链接粘贴进去。

## Exercise 3 : LeetCode 练习：链表进阶

继续完成链表相关算法练习：

https://labuladong.online/zh/algo/essential-technique/linked-list-skills-summary/

在 LeetCode 上完成以下 2 个练习，并截图提交：

[86. 分隔链表](https://leetcode.cn/problems/partition-list/)

[19. 删除链表的倒数第 N 个结点](https://leetcode.cn/problems/remove-nth-node-from-end-of-list/)

## Game start
readme.md 完成day1

最实用的顺序就是这个：


1. 先让 parse() 能读 board_simple.txt
2. 再让 grid_to_string() 能打印地图
3. 再让玩家可以 d / a / w / s 移动
4. 再加撞墙判断
5. 再加 W 水桶
6. 再加 F 火
7. 再加 1-9 传送门
8. 最后加胜利、失败、退出、非法输入