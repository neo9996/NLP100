#coding UTF-8
import itertools

f = "hightemp.txt"
col1 = []
col2 = []
with open(f, 'r') as data_file:
    for line in data_file:
        row = line.split("\t")
        col1.append(row[0])

for k, g in itertools.groupby(sorted(col1)):
        a = k, len([i for i in g])
        col2.append(a)

ans = sorted(col2, key=lambda x: x[1], reverse=True)
for i in range(len(ans)):
    print(str(ans[i][0]) + " " + str(ans[i][1]))

# UNIX操作
# sort cat hightemp.txt | cut -f1 | sort | uniq -c | sort -r
