#N = list(map(str, input().split()))
import random
N = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
L = N.split()
l = len(L)
A = []
for i in range(l):
    if len(L[i]) <= 4:
        A.append(L[i])
    else:
        li = list(L[i])
        word = li[1:len(li)-1]
        re_word = []
        random.shuffle(word)
        re_word.append(li[0])
        s = "".join(map(str, word))
        re_word.append(s)
        re_word.append(li[len(li)-1])
        a = "".join(map(str, re_word))
        A.append(a)
ans = " ".join(map(str, A))
print(ans)
