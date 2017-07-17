#coding UTF-8

f = "hightemp.txt"
with open(f, 'r') as data_file, \
    open('col1.txt', 'w') as wf1, \
    open('col2.txt', 'w') as wf2:
            for line in data_file:
                row = line.split("\t")
                wf1.write(row[0] + "\n")
                wf2.write(row[1] + "\n")
# UNIX操作
# cut -f 1 > hightemp.txt
# cat col1.txt
# cut -f 2 > hightemp.txt
# cat col2.txt
