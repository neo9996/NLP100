#N = "abcdefg"
N = input()
L = list(N)
l = len(L)
A = []


def cipher(L):
    for i in range(l):
        if L[i].islower() == True:
            a = ord(L[i])
            b = chr(219-a)
            A.append(b)
        else:
            A.append(L[i])

cipher(L)
ans = "".join(map(str, A))
print("暗号化:" + ans)

A = []
cipher(ans)
ans2 = "".join(map(str, A))
print("復号化:" + ans2)
