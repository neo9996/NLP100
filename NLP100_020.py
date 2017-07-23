#coding UTF-8
import json
import gzip

f = "jawiki-country.json.gz"

with gzip.open(f, 'r') as data_file:
    for line in data_file:
        obj = json.loads(line)
        if obj['title'] == 'イギリス':
            print(obj['text'])
