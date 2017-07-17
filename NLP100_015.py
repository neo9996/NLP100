#coding UTF-8

N = int(input())
f = "hightemp.txt"
c = 0
with open(f) as data_file:
    for line in data_file:
        c += 1

f = open("hightemp.txt")
word = f.readlines()[c-N:c]

for line in word:
    ans = "".join(map(str, word))
print(ans.rstrip())

# UNIX操作
# tail -n 10 hightemp.txt
