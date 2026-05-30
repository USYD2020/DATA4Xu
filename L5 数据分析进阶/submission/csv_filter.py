import csv
reader = csv.reader(open('climate_data_2017.csv'),delimiter=',')
writer = csv.writer(open('output.csv','w'))
for i,row in enumerate(reader):
    if i == 0:
        writer.writerow(row)
        continue
    if row[1] == 'NSW':
        writer.writerow(row)