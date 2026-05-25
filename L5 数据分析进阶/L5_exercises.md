# L5 数据分析进阶练习题集

这次三道题都围绕气象数据。第一题练习 Python 内置 `csv` 模块，后两题练习 pandas。重点是看清楚数据列，再做筛选、分组和统计。

## Exercise 1: 筛选 NSW 数据 ⭐

从气候数据里筛选出所有 `NSW` 的记录，并写入一个新的 CSV 文件。

这题请在 `csv/` 文件夹里完成，因为数据文件和脚本都放在这个子目录里。

**要求：**

1. 导入 Python 内置的 `csv` 模块
2. 读取 `climate_data_2017.csv`
3. 创建一个新的输出文件 `output.csv`
4. 用 `csv.reader()` 读取原始文件
5. 用 `csv.writer()` 写入新文件
6. 保留第 1 行表头
7. 对其他数据行，只保留第 2 列为 `NSW` 的记录
8. 建议用写入模式创建 `output.csv`，避免重复运行时一直追加旧结果

### 测试代码 + 预期输出

```python
python3 csv_filter.py
# 运行后会生成 output.csv
# output.csv 第一行是表头
# 后面的每一行第二列都应该是 NSW
```

### 代码框架

```python
import csv

reader = csv.reader(open("climate_data_2017.csv"), delimiter=",")
writer = csv.writer(open("output.csv", "w"))

for i, row in enumerate(reader):
    # i == 0 是表头，需要保留
    # row[1] 是 state 列
    # 如果这一行应该保留，就写入 output.csv
    pass
```

---

## Exercise 2: 找出高温天最大降雨量 ⭐⭐

找出所有最高温超过 35°C 的日子，然后计算这些高温天里最大的降雨量是多少。

这题用 pandas 来做。注意列名要写完整，包括空格和括号。

**要求：**

1. 导入 `pandas as pd`
2. 用 `pd.read_csv()` 读取 `climate_data_2017.csv`
3. 使用 `Maximum temperature (C)` 这一列判断是否为高温天
4. 高温天定义为最高温大于 35°C
5. 用布尔筛选拿到所有高温天记录
6. 在高温天中，找出 `Rainfall (mm)` 的最大值
7. 按指定格式打印结果

### 测试代码 + 预期输出

```python
python3 pandas_summer_rain.py
# Maximum amount of rainfall on hot days: 67.3 mm
```

### 代码框架

```python
import pandas as pd

df = pd.read_csv("climate_data_2017.csv")

# 先做一个 True/False 条件：哪些行是高温天
is_hot_day = None

# 用上面的条件筛选出高温天
hot_days = None

# 在高温天里找 Rainfall (mm) 的最大值
max_rain = None

print("Maximum amount of rainfall on hot days:", float(max_rain), "mm")
```

---

## Exercise 3: 按州统计最大湿度 ⭐⭐⭐

按 `State` 分组，找出每个州早上 9 点相对湿度的最大值，然后按州名字母顺序输出。

这题重点是 `groupby`：先把同一个州的数据放到一组，再对每组做统计。

**要求：**

1. 导入 `pandas as pd`
2. 用 `pd.read_csv()` 读取 `climate_data_2017.csv`
3. 用 `State` 这一列分组
4. 对每个州，取 `9am relative humidity (%)` 的最大值
5. 可以把结果转成字典，方便遍历
6. 按州名字母顺序输出
7. 输出格式为 `州名 : 最大湿度`

### 测试代码 + 预期输出

```python
python3 groupby.py
# NSW : 91.0
# QLD : 94.0
# SA : 88.0
# TAS : 96.0
# VIC : 86.0
# WA : 82.0
```

### 代码框架

```python
import pandas as pd

df = pd.read_csv("climate_data_2017.csv")

# 按 State 分组
grouped_by_state = None

# 对每个州，取 9am relative humidity (%) 的最大值
max_humidity_by_state = None

# 可以转成字典，再按 key 排序输出
max_humidity_by_state_as_dict = None

for k in sorted(max_humidity_by_state_as_dict):
    print(k, ":", float(max_humidity_by_state_as_dict[k]))
```

\---

## Exercise 4 : LeetCode 练习：双指针

完成 数组相关的双指针算法阅读

https://labuladong.online/zh/algo/essential-technique/array-two-pointers-summary-2/

[1. 两数之和](https://leetcode.cn/problems/two-sum/)

[704. 二分查找](https://leetcode.cn/problems/binary-search/)

[344. 反转字符串](https://leetcode.cn/problems/reverse-string/)
