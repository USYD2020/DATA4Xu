# ============================================================
# 问题：从气候数据CSV文件中，筛选出所有属于NSW的数据行，
#       并将结果写入一个新的CSV文件中。
# ============================================================

import csv
# Abtraction 抽象 use it without knowing details of implementation

# 打开原始数据文件，创建一个 CSV 读取器
# csv.reader() 会把每一行变成一个列表（list），方便我们按索引访问每个字段
reader = csv.reader(open('climate_data_2017.csv'), delimiter=',')

# 打开（或创建）一个新的输出文件，'w' 表示写入模式
# csv.writer() 帮我们把列表格式的数据写回 CSV 格式, w for write 覆写
writer = csv.writer(open('output.csv', 'a'))

# enumerate(reader) 让我们同时获得「行号 i」和「行内容 row」
# i = 0 是表头（header），我们一定要保留
# row[1] 是第二列，也就是 "State" 列
# Enumerate:[a,b,c] => [(0,a),(1,b),(2,c)]
for i, row in enumerate(reader):
    if i == 0 or row[1] == 'NSW':   # 保留表头 OR 该行是NSW的数据
        writer.writerow(row)         # 把符合条件的行写入新文件

# 💡 知识点：
# 1. csv 模块是 Python 内置的，专门处理 CSV 文件的读写
# 2. enumerate() 可以在遍历时同时获取索引和元素
# 3. 条件筛选：用 if 语句决定哪些行需要保留
# 4. csv.reader() 会自动读取列表
# 5. csv.writer() 会自动加一行
