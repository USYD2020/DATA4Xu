# L6 Colab 大数据分析练习题集

这两道题都在 **Google Colab** 上完成。操作步骤：
1. 打开 [Google Colab](https://colab.research.google.com/)
2. 新建一个 Notebook
3. 把数据文件上传到 Colab（点击左侧文件夹图标，然后上传）
4. 在代码格里写代码，运行看结果

完成后把你的 **Colab 链接** 放到 `submission` 文件夹下。

---

## Exercise 1: 找出高温天最大降雨量 ⭐⭐

这题来自 L5，没做完的在这里继续。

找出所有最高温超过 35°C 的日子，然后计算这些高温天里最大的降雨量是多少。

你需要上传 **L5 的原始数据文件** `Climate_data_2017.csv`（注意大写 C）。这个文件有 6 列，列名分别是：
- `Date`
- `Maximum temperature (C)`
- `Rainfall (mm)`
- `Minimum temperature (C)`
- `State`
- `9am relative humidity (%)`

**要求：**

1. 导入 `pandas as pd`
2. 用 `pd.read_csv()` 读取上传的数据文件
3. 用 `Maximum temperature (C)` 这一列判断是否为高温天（大于 35°C）
4. 用布尔筛选拿到所有高温天记录
5. 在高温天中，找出 `Rainfall (mm)` 的最大值
6. 按指定格式打印结果

### 测试代码 + 预期输出

```python
# Maximum amount of rainfall on hot days: 67.3 mm
```

### 代码框架

```python
import pandas as pd

df = pd.read_csv("Climate_data_2017.csv")

# 先做一个 True/False 条件：哪些行是高温天
is_hot_day = None

# 用上面的条件筛选出高温天
hot_days = None

# 在高温天里找 Rainfall (mm) 的最大值
max_rain = None

print("Maximum amount of rainfall on hot days:", float(max_rain), "mm")
```

---

## Exercise 2: 统计 2017 年各风向出现天数 ⭐⭐⭐

统计 2017 年各个风向出现了多少天，按风向字母顺序输出。

你需要上传 `test/climate_data_2017.csv`。这个文件有 `date` 和 `wind_dir` 两列，我们主要用这两列。

思路：先拿到数据里所有可能的风向并排序，再按风向分组统计 2017 年的出现次数。如果某个风向在 2017 年没出现，输出 0。

**要求：**

1. 导入 `pandas as pd`
2. 读取 `test/climate_data_2017.csv`
3. 用 `wind_dir` 列获取所有可能的风向并排序
4. 筛选出 2017 年的数据（`date` 列以 `"2017"` 开头）
5. 按 `wind_dir` 分组，统计每个风向出现的次数
6. 遍历所有风向，有出现就输出次数，没出现就输出 0

### 测试代码 + 预期输出

```python
# E : 8
# N : 7
# NE : 5
# NW : 2
# S : 9
# SE : 4
# SW : 7
# W : 6
```

### 代码框架

```python
import pandas as pd

df = pd.read_csv("test/climate_data_2017.csv")

# 获取所有可能的风向，排序
all_wind_dirs = None

# 筛选 2017 年数据，按 wind_dir 分组计数
grouped_data_2017 = None
wind_dir_counts = None

# 遍历所有风向，输出计数
for d in all_wind_dirs:
    value = wind_dir_counts.get(d, 0)
    print(f"{d} : {value}")
```

---

## 提交说明

完成后，在 `submission` 文件夹下新建一个文件（比如 `你的名字_L6.txt`），把你的 Colab Notebook 链接粘贴进去。

<img src="/Users/gogo/Library/Application Support/typora-user-images/image-20260530235342630.png" alt="image-20260530235342630" style="zoom:50%;" />

## Exercise 3 : LeetCode 练习：二分查找

完成 二分查找 相关的双指针算法阅读

https://labuladong.online/zh/algo/essential-technique/binary-search-framework/

在 LeetCode 上完成以下两个练习，并截图提交：

[704. 二分查找](https://leetcode.cn/problems/binary-search/)

[34. 在排序数组中查找元素的第一个和最后一个位置](https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/)
