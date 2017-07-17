#N = input()
N = "I am an NLPer"

def bigram(N):
    li = [(i+j) for (i,j) in zip(N,N[1:])]
    print(li)

def word_bigram(M):
    li = []
    l = len(M)
    for i in range(0, l-1):
        li.append(M[i:i+2])
    print(li)

M = N.split()
word_bigram(M)
bigram(N)
#trigram(N)
