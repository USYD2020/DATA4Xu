is_first_line = True
hd_count = {}
units = set()
for row in open('inp.txt'):
    if is_first_line:
        is_first_line = False
        continue
    else:
        name, unikey, unit, year, mark = row.strip('\n').split(':')
        if '1001' in unit:
            units.add(unit)
        if unit not in hd_count:
            hd_count[unit] = 0
        if int(mark) <= 60:
            hd_count[unit] += 1
for i in hd_count:
    print(f'{i} {hd_count[i]}')