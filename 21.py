# 连接mongodb
import pymongo
client = pymongo.MongoClient('localhost', 27017)
walden = client['walden']
sheet_lines = walden['sheet_lines']

path = 'C:\\站点资源\\小说\\test.txt'
with open(path, 'r',encoding='utf-8') as f:
  lines = f.readlines()
  for index,line in enumerate(lines):
    data = {
      'index': index,
      'line': line,
      'word': len(line)
    }
    sheet_lines.insert_one(data)

# for item in sheet_lines.find({'index': 1}):
#   print(item)