# ============================================================
# Exercise 1 — 各州平均降雨量
# Method 1: 使用 Python 原生方法 with open 读取
# ============================================================
# 这是 L3/L4 就开始练的套路：
#   open → 跳标题 → split → 字典收集 → 手动统计
# pandas 的 groupby().mean() 背后做的就是这些事。
# ============================================================

rain_by_state = {}

with open("climate_data_2017.csv") as f:
    next(f)  # 跳过标题行（date,state,city,...）
    for row in f:
        values = row.strip().split(",")

        state = values[1]              # 第 2 列：州名
        rainfall = float(values[6])    # 第 7 列：降雨量

        # 如果这个州第一次出现，先创建空列表
        if state not in rain_by_state:
            rain_by_state[state] = []

        # 把这条记录的降雨量追加进去
        rain_by_state[state].append(rainfall)

# 按州名字母顺序遍历，计算平均值
for state in sorted(rain_by_state):
    rain_list = rain_by_state[state]
    avg = sum(rain_list) / len(rain_list)
    print(state, ":", round(avg, 1))

# 💡 知识点：
# 1. with open() as f → 安全打开文件，结束后自动关闭
# 2. next(f) → 跳过第一行标题
# 3. strip() + split(",") → 去掉换行 + 按逗号拆字段
# 4. 字典 key=州名, value=列表 → 收集同一个州的所有降雨量
# 5. sum(list)/len(list) → 手动求平均

'''output
NSW : 2.1
QLD : 5.1
SA : 2.8
TAS : 2.5
VIC : 2.7
WA : 7.8
'''
