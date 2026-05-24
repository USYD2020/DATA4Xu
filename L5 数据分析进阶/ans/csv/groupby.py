# ============================================================
# 问题：按州（State）分组，找出每个州【相对湿度】的最大值，并按州名字母顺序输出。
# ============================================================

import pandas as pd

# 读取12月的气候数据
df = pd.read_csv('climate_data_2017.csv')

# groupby('State')：按 "State" 列分组
# 相当于把同一个州的所有数据放在一起
grouped_by_state = df.groupby('State')

# 对每个分组，取出 '9am relative humidity (%)' 列，求最大值
# 结果是一个 Series：索引是州名，值是该州的最大湿度
max_humidity_by_state = grouped_by_state['9am relative humidity (%)'].max()

# 转换为字典，方便遍历和格式化输出
max_humidity_by_state_as_dict = max_humidity_by_state.to_dict()

# sorted() 对字典的键（州名）进行字母排序，然后逐个打印
for k in sorted(max_humidity_by_state_as_dict):
    print(k, ':', float(max_humidity_by_state_as_dict[k]))

# 💡 知识点：
# 1. df.groupby('列名') → 按某列分组，返回 GroupBy 对象
# 2. GroupBy对象['列名'].max() → 对每组求最大值
# 3. .to_dict() → 把 Series 转为 Python 字典
# 4. sorted(dict) → 对字典的键排序后遍历

'''output
NSW : 91.0
QLD : 94.0
SA : 88.0
TAS : 96.0
VIC : 86.0
WA : 82.0
'''