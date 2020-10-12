
# git remote add origin https://github.com/xucasio/python_cartoon.git
# git branch -M main
# git push -u origin main

# 连接mongodb
import pymongo
import os
client = pymongo.MongoClient('localhost', 27017)
walden = client['walden']
sheet_lines = walden['sheet_lines']

path = os.getcwd() + '\\files\\test.txt'
with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for index, line in enumerate(lines):
        data = {'index': index, 'line': line, 'word': len(line)}
        sheet_lines.insert_one(data)

# for item in sheet_lines.find({'index': 1}):
#   print(item)