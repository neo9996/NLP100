#coding UTF-8

f = "hightemp.txt"
col1 = []
with open(f, 'r') as data_file:
    for line in data_file:
        row = line.split("\t")
        col1.append(row)
col2 = sorted(col1, key=lambda x: x[2])
for n in col1:
    ans = " ".join(map(str, n))
    print(ans.rstrip())

# UNIX操作
# sort -k3,1nr hightemp.txt
