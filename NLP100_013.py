#coding UTF-8

f = "col3.txt"
with open(f, 'w') as wf1, \
    open('col1.txt', 'r') as rf1, \
    open('col2.txt', 'r') as rf2:
            for (i, j) in zip(rf1, rf2):
                wf1.write(i.rstrip("\r\n") + "\t" + j)
# UNIX操作
# paste col1.txt col2.txt > col_sample.txt
