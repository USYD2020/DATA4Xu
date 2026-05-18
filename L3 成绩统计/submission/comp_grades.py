is_first_line = True
hd_count = {}
for row in open('inp.txt'):
    if is_first_line:
        is_first_line = False
        continue
    else:
        name, unikey, unit, year, mark = row.strip('\n').split(':')
        if unikey not in hd_count:
            hd_count[unikey] = 0
        if year == '2016' and int(mark) >= 85:
            hd_count[unikey] += 1
for i in hd_count:
    print(f'{i} {hd_count[i]}')