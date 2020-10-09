# ab字符之间的内容
import re
# 匹配两个字符中间的所有字符
a = '<p>life is short, i use python<a/>i love it<p>'

r = re.search('<p>(.*)<a/>(.*)<p>', a)

print(r)