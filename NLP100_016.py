#coding UTF-8

import math

N = int(input())
f = "hightemp.txt"
a = math.ceil(24 / N)
A = 0

with open(f, 'r') as data_file:
    lines = data_file.readlines()

for i in range(N):
    with open('col016' + str(i+1) + '.txt',  'w') as wf:
        word = lines[A:A+a]
        wf.writelines(word)
        A += a

# UNIX操作
# split -l N(任意の数N) hightemp.txt col016
