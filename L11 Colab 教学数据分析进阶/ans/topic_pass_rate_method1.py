# ============================================================
# Exercise 1 — 各 Python 主题平均测试通过率
# Method 1: 使用 Python 原生方法 with open 读取
# ============================================================
# open → 跳标题 → split → 计算 pass_rate → 字典收集 → 手动统计
# 这是理解 pandas 新列计算和 groupby().mean() 的基础。
# ============================================================

pass_rates_by_topic = {}

with open("python_learning_log.csv") as f:
    next(f)  # 跳过标题行
    for row in f:
        values = row.strip().split(",")

        topic = values[2]                    # 第 3 列：Python 学习主题
        tests_passed = float(values[4])      # 第 5 列：通过测试数
        tests_total = float(values[5])       # 第 6 列：总测试数

        # 每条记录的测试通过率
        pass_rate = tests_passed / tests_total

        # 如果这个 topic 第一次出现，先创建空列表
        if topic not in pass_rates_by_topic:
            pass_rates_by_topic[topic] = []

        # 把这条记录的通过率追加进去
        pass_rates_by_topic[topic].append(pass_rate)

# 按 topic 字母顺序遍历，计算平均通过率
for topic in sorted(pass_rates_by_topic):
    rates = pass_rates_by_topic[topic]
    avg_rate = sum(rates) / len(rates)
    print(topic, ":", round(avg_rate * 100, 1), "%")

# 💡 知识点：
# 1. with open() as f → 安全打开文件，结束后自动关闭
# 2. next(f) → 跳过第一行标题
# 3. pass_rate = tests_passed / tests_total → 从原始列计算新指标
# 4. 字典 key=topic, value=通过率列表 → 收集同一主题的数据
# 5. avg_rate * 100 → 把小数通过率转换成百分比

'''output
dictionaries : 76.7 %
file_io : 77.5 %
functions : 76.0 %
lists : 80.0 %
loops : 77.5 %
pandas_groupby : 70.0 %
pandas_intro : 76.0 %
variables : 88.0 %
'''
