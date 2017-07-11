# coding: utf-8
S = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
dic = {}
word = S.split()
#a = [1, 5, 6, 7, 8, 9, 15, 16, 19]
a = [0, 4, 5, 6, 7, 8, 14, 15, 18]
for (i, x) in enumerate(word):
    if i in a:
        dic[word[i][0:1]] = i + 1
    else:
        dic[word[i][0:2]] = i + 1
print(dic)
