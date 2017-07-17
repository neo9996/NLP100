#coding UTF-8

N = int(input())
f = open("hightemp.txt")
#with open(f, 'r') as data_file:
#    for line in data_file:
#for line in open(f, 'r'):
word = f.readlines()[0:N]

for line in word:
    ans = "".join(map(str, word))
print(ans.rstrip())

# UNIX操作
# cat hightemp.txt | head - 10
