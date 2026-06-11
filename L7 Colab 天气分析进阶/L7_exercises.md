# L7 Colab 天气分析进阶练习题集

这两道题继续在 **Google Colab** 上完成。操作步骤：
1. 打开 [Google Colab](https://colab.research.google.com/)
2. 新建一个 Notebook
3. 把数据文件上传到 Colab（点击左侧文件夹图标，然后上传）
4. 在代码格里写代码，运行看结果

完成后把你的 **Colab 链接** 放到 `submission` 文件夹下。

两道题都用 L6 的数据文件 `climate_data_2017.csv`（就是 L6 里 `test/` 文件夹下那个）。这个文件有 13 列，我们这次主要用这几列：
- `date`（日期，格式是 `2017-01-03` 这样）
- `state`（州名）
- `rainfall`（降雨量）
- `temp9am`（上午 9 点温度）

---

## Exercise 1: 各州平均温度排名 ⭐⭐

算出每个州上午 9 点温度的平均值，然后**从高到低**排序输出。

L5/L6 我们用 `groupby` 之后求过 `.max()` 和 `.size()`，这次换成求平均值 `.mean()`，再加一个新朋友：排序函数 `sort_values()`。

**要求：**

1. 导入 `pandas as pd`
2. 用 `pd.read_csv()` 读取 `climate_data_2017.csv`
3. 用 `state` 这一列分组
4. 对每个州，取 `temp9am` 的平均值
5. 用 `sort_values()` 把结果按平均温度**从高到低**排序（想想 `ascending` 参数该填什么）
6. 遍历排序后的结果，输出 `州名 : 平均温度`
7. 平均温度保留 1 位小数，用 `round(..., 1)`

### 测试代码 + 预期输出

```python
# WA : 27.1
# QLD : 25.0
# NSW : 21.8
# SA : 20.3
# VIC : 16.8
# TAS : 13.5
```

### 代码框架

```python
import pandas as pd

df = pd.read_csv("climate_data_2017.csv")

# 按 state 分组，对 temp9am 求平均值
avg_temp_by_state = None

# 按平均温度从高到低排序
sorted_avg_temp = None

# 遍历排序后的结果，输出
# 提示：Series 可以用 .items() 遍历，每一项是 (州名, 平均温度)
for state, temp in sorted_avg_temp.items():
    print(state, ":", round(float(temp), 1))
```

---

## Exercise 2: 找出每个州雨下得最多的月份 ⭐⭐⭐

对每个州，找出 2017 年**总降雨量最大**的那个月，输出州名、月份和那个月的总降雨量。

这题分三步走：

1. 先从 `date` 列里取出月份（比如 `2017-01-03` 的月份是 `01`），存成新的一列
2. 按 `state` 和 `month` **两列一起**分组，对 `rainfall` 求和——这是第一次用两列做 groupby，分组的 key 会变成 `(州名, 月份)` 这样的元组
3. 在每个州自己的所有月份里，挑出总降雨量最大的那个月

第三步可以把求和结果转成字典再遍历，就跟 L4 Exercise 2 用 `(month, state)` 当 key 找最大值的套路一样，只是这次数据是 pandas 算好的。

**要求：**

1. 导入 `pandas as pd`
2. 读取 `climate_data_2017.csv`
3. 从 `date` 列提取月份，存成新列 `month`（提示：`df["date"].str.split("-").str[1]`）
4. 用 `groupby(["state", "month"])` 按两列分组
5. 对 `rainfall` 求和
6. 把结果转成字典，key 是 `(state, month)` 元组
7. 遍历字典，对每个州记录总降雨量最大的月份
8. 按州名字母顺序输出：`州名 : 月份 : 总降雨量`
9. 总降雨量保留 1 位小数

### 测试代码 + 预期输出

```python
# NSW : 05 : 4.4
# QLD : 02 : 13.5
# SA : 04 : 6.0
# TAS : 01 : 5.6
# VIC : 06 : 6.2
# WA : 02 : 16.2
```

### 代码框架

```python
import pandas as pd

df = pd.read_csv("climate_data_2017.csv")

# 从 date 列提取月份，存成新列
df["month"] = None

# 按 state 和 month 两列分组，对 rainfall 求和
rain_by_state_month = None

# 转成字典，key 长这样：(state, month)
rain_dict = None

# 对每个州，找出总降雨量最大的月份
# 提示：再建一个字典 best，key 是州名，value 是 (月份, 总降雨量)
best = {}
for (state, month), total in rain_dict.items():
    # 如果这个州第一次出现，直接存进去
    # 如果这个州已经有记录，比较一下，留下降雨量更大的那个月
    pass

# 按州名字母顺序输出
for state in sorted(best):
    month, total = best[state]
    print(state, ":", month, ":", round(float(total), 1))
```

### 这题在练什么

1. `.str.split()` 可以对一整列字符串做拆分，不用自己写循环
2. `groupby` 可以传一个列表，按多列分组，key 变成元组
3. pandas 算完不等于做完——“组内找最大”这一步还是回到 L4 学过的字典套路
4. 输出前别忘了排序要求是按州名，不是按降雨量

---

## 提交说明

完成后，在 `submission` 文件夹下新建一个文件（比如 `你的名字_L7.txt`），把你的 Colab Notebook 链接粘贴进去。

## Exercise 3 : LeetCode 练习：滑动窗口

完成 滑动窗口算法框架 的阅读

https://labuladong.online/zh/algo/essential-technique/sliding-window-framework/

在 LeetCode 上完成以下两个练习，并截图提交：

[209. 长度最小的子数组](https://leetcode.cn/problems/minimum-size-subarray-sum/)

[3. 无重复字符的最长子串](https://leetcode.cn/problems/longest-substring-without-repeating-characters/)
