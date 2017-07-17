#coding UTF-8

f = open("hightemp.txt")
ans = f.readlines()
count = 0
for line in ans:
    count += 1
print(count)

# UNIX操作
# wc -l hightemp.txt
