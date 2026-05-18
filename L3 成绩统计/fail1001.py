# 问题描述：
# 给定一个名为 'inp.txt' 的文本文件，每一行为一个学生的一条成绩记录，各字段用冒号（:）分隔。
# 第一行为表头，从第二行起，每行包含如下格式的数据：
#    姓名:学号:课程编号:成绩
# 要求你编写程序，统计所有以 '1001' 结尾的课程编号中，不同挂科（成绩<50）学生的人数。
# 程序输出每个以'1001'结尾的课程编号及其挂科学生人数（没有挂科学生则输出0），每行为：
#    课程编号 挂科人数
#   elec1001 0
#   engg1001 1
#   buss1001 0
# 输出顺序可以任意。
# 使用 Dictionary 字典以及集合 set 语法来解决下面这道题：找到以 1001 结尾的课程编号及其挂科人数，然后打印出来。

is_first_line = True
fail_count = {}
units = set()

for row in open('inp.txt'):
    if is_first_line:
        is_first_line = False
    else:
        values = row.strip('\n').split(':')
        unikey = values[1]
        unit = values[2]
        mark = int(values[-1])
        
        if unit[-4:] == '1001':
            units.add(unit)
            if mark < 50:
                if unit not in fail_count:
                    fail_count[unit] = [unikey]
                # 仅添加未出现过的学生
                elif unikey not in fail_count[unit]:
                    fail_count[unit].append(unikey)

for unit in units:
    if unit in fail_count:
        print(unit, len(fail_count[unit]))
    else:
        print(unit, 0)
		
