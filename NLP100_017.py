#coding UTF-8

f = "hightemp.txt"
col1 = set()
with open(f, 'r') as data_file:
    for line in data_file:
        row = line.split("\t")
        col1.add(row[0])
for n in col1:
    print(n)

# UNIX操作
# cut -f1 hightemp.txt | sort | uniq
