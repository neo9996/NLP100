#coding UTF-8

f = "hightemp.txt"

for line in open(f, 'r'):
    item = "".join(line).replace("\t", " ")
    print(item, end='')

# UNIX操作
# expand -t 1 hightemp.txt > new_high.txt
# cat new_high.txt
