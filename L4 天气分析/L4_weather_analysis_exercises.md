# L4 天气分析练习题集

这次我们用同一个气象数据文件 `climate_data_2017.csv` 做两道小分析题。重点不是复杂算法，而是练习：读文件、跳过标题行、拆字段、取出需要的列，再用字典做统计。

## Exercise 1: 统计高湿度天数 ⭐

文件里每一行是一条城市气象记录。你要统计：有多少个不同日期，上午 9 点湿度大于 80。

注意，同一天可能有多个城市记录。只要这一天有任意一条记录的湿度大于 80，这一天就算 1 次，但同一天不能重复计数。

**要求：**

1. 读取 `climate_data_2017.csv`
2. 跳过第一行标题
3. 用 `split(',')` 拆开每一行
4. 日期在第 1 列，也就是 `values[0]`
5. 上午 9 点湿度在第 13 列，也就是 `values[12]`
6. 只统计湿度大于 80 的日期
7. 同一个日期只统计一次
8. 最后打印符合条件的天数

### 测试代码 + 预期输出

```python
python3 humidDays.py
# There were 6 days with humidity greater than 80
```

### 代码框架

```python
humid_days = {}
is_first_line = True

for row in open("climate_data_2017.csv"):
    if is_first_line:
        is_first_line = False
    else:
        values = row.split(",")
        date = values[0]
        humidity = float(values[12])

        # 如果湿度大于 80，把这个日期记下来
        # 提示：字典的 key 可以用日期
        pass

print("There were", len(humid_days), "days with humidity greater than 80")
```

---

## Exercise 2: 找出“最低降雨量最高”的月份和州 ⭐⭐⭐

这题听起来绕，其实分两步：

先看每个月、每个州，找出它自己的单日最小降雨量。然后在这些“最小降雨量”里面，再找出最大的那一个。

比如某个州某个月的几天降雨量是 `6.8, 5.9, 8.4`，那这个州这个月的单日最小降雨量就是 `5.9`。

**要求：**

1. 读取 `climate_data_2017.csv`
2. 跳过第一行标题
3. 用 `split(',')` 拆开每一行
4. 日期在第 1 列，可以从日期里取月份
5. 州名在第 2 列，也就是 `values[1]`
6. 降雨量在第 7 列，也就是 `values[6]`
7. 用 `(month, state)` 作为字典 key
8. 统计每个 `(month, state)` 对应的单日最小降雨量
9. 找出这些最小降雨量里面最大的那一组
10. 打印月份和州名

### 测试代码 + 预期输出

```python
python3 min_month_state.py
# Month: 06
# State: WA
```

### 代码框架

```python
min_mth_rain = {}

with open("climate_data_2017.csv") as f:
    next(f)
    for row in f:
        values = row.split(",")
        month = values[0].split("-")[1]
        state = values[1]
        rainfall = float(values[6])
        key = (month, state)

        # 如果 key 已经出现过，更新成更小的 rainfall
        # 如果 key 第一次出现，直接存进去
        pass

# 在 min_mth_rain 里面找 value 最大的那一组
# 提示：items() 里面每一项长这样：((month, state), rainfall)

print("Month:", month)
print("State:", state)
```

---

## Exercise 3 : LeetCode 练习：快慢指针

完成 数组相关的双指针算法阅读
https://labuladong.online/zh/algo/essential-technique/array-two-pointers-summary-2/

[26. 删除有序数组中的重复项](https://leetcode.cn/problems/remove-duplicates-from-sorted-array/)

[27. 移除元素](https://leetcode.cn/problems/remove-element/)

[283. 移动零](https://leetcode.cn/problems/move-zeroes/)

完成以上三个练习并提交成功后，把提交记录的截图存储在 submission 文件夹中。
