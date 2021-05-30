import xlrd

file_path = 'magic_formula_data.xlsx'
wd = xlrd.open_workbook(file_path)

per_sh = wd.sheet_by_name('PER')

per_dict = {}
for i in range(1, per_sh.nrows):
    data = per_sh.row_values(i) #한 줄의 row
    name = data[0]
    per = data[1]
    if per > 0:
        per_dict[name] = per

sorted(per_dict)

import operator
roa_sh = wd.sheet_by_name('ROA')

roa_dict = {}
for i in range(1, roa_sh.nrows):
    data = roa_sh.row_values(i)
    name = data[0]
    roa = data[1]
    if roa > 0:
        roa_dict[name] = roa

sorted(roa_dict)

sorted_per = sorted(per_dict.items(), key=operator.itemgetter(1))
sorted_roa = sorted(roa_dict.items(), key=operator.itemgetter(1))

per_rank = {}

for num, firm in enumerate(sorted_per):
    per_rank[firm[0]] = num + 1

print(per_rank)

roa_rank = {}

for num, fir in enumerate(sorted_roa):
    roa_rank[firm[0]] = num + 1

print(roa_rank)

roa_rank = {}

total_rank = {}
for name in roa_rank.keys():
    if name in per_rank.keys():
        total_rank[name] = per_rank[name] + roa_rank[name]

print(total_rank)

sorted_total = sorted(total_rank.items(), key=operator.itemgetter(1))

print(sorted_total)