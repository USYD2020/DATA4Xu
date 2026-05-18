# 问题描述：
# 给定一个名为 'inp.txt' 的文本文件，文件的每一行记录了学生的成绩信息，格式如下：
# name:unikey:something:...:year:mark
# （例如：John Smith:z5111111:...:2016:87）
# 第一行为表头，请跳过。
# 请你统计每个学生（unikey）在 2016 年取得高于等于 85 分（即 mark >= 85）的成绩的次数，
# 并输出每个学生的 unikey 以及对应的次数，每行输出一个学生。
#
# 例如，如果 z5111111 在 2016 年有两门课程 mark>=85，则输出：
# z5111111 2
# 按照输入文件出现的顺序输出每个学生的统计数据。

is_first_line = True
hd_count = {}
for row in open('inp.txt'):
    if is_first_line:
        is_first_line = False
    else:
        values = row.strip('\n').split(':')
        unikey = values[1]
        year = values[-2]
        mark = int(values[-1])
        
        #boolean can be used in computation as 1 or 0
        is_above_86_in_2016 = mark >=85 and year == '2016'
        if unikey not in hd_count:
            hd_count[unikey] = int(is_above_86_in_2016) # 0 + is_above_86_in_2016
        else:
            hd_count[unikey] += int(is_above_86_in_2016)

for unikey, count in hd_count.items():
    print(unikey,count)
		
