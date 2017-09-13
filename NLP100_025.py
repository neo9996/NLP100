#coding UTF-8
import json
import gzip
import re

f = "jawiki-country.json.gz"

def UK():
    with gzip.open(f, 'r') as data_file:
        for line in data_file:
            obj = json.loads(line)
            if obj['title'] == 'イギリス':
                return obj['text']

pattern = r'^\{\{基礎情報 国(.*?)\}\}$'
repatter = re.compile(pattern, re.MULTILINE + re.DOTALL)
sentence = repatter.findall(UK())

pattern = r'^(?:\|)(.*)\s=\s(.*?)$'
repatter = re.compile(pattern, re.MULTILINE)
answer = repatter.findall(sentence[0])

for k in answer:
    print(k)
