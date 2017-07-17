#N = input()
X = "paraparaparadise"
Y = "paragraph"

def bigram(N):
    li = [(i+j) for (i,j) in zip(N,N[1:])]
    #print(li)
    return li

def word_bigram(M):
    li = []
    l = len(M)
    for i in range(0, l-1):
        li.append(M[i:i+2])
    #print(li)
    return li

X = bigram(X)
Y = bigram(Y)
print(X)
print(Y)
set_X = set(X)
set_Y = set(Y)

wa_list = set_X.union(set_Y)
print(wa_list)

seki_list = list(set_X & set_Y)
print(seki_list)

sa_list = set(X).symmetric_difference(set(Y))
print(sa_list)

ansX = "se" in X
ansY = "se" in Y
print(ansX)
print(ansY)
