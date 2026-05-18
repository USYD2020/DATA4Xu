is_first_line = True
hd_count = {}

for row in open('inp.txt'):
    if is_first_line:
        # 跳过第一行表头
        is_first_line = False
        continue

    # 拆字段
    values = row.strip('\n').split(':')

    # 取出 unikey, year, mark
    _, unikey, unit, year, mark = values
    # print(unikey, unit, year, mark)

    # 判断这一行是不是 2016 年的高分
    if int(mark) >= 85 and year == '2016':
        # 如果这个学生第一次出现，先在字典里放一个初始值
        if unikey not in hd_count:
            hd_count[unikey] = 0

        # 否则更新这个学生的次数
        hd_count[unikey] += 1

# 输出每个学生的统计结果
for unikey, count in hd_count.items():
    print(unikey, count)