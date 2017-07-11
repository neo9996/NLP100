# coding: utf-8
import re
sentence = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
array = []
#word = sentence.split(" ")
word = re.sub('[.,]', '', sentence)
word = word.split()
l = len(word)
print(word)
for i in range(l):
    count = list(word[i])
    len2 = len(count)
    array.append(len2)
print(array)
