#!/usr/bin/python3
import re
 
# line = "Cats are smarter than dogs"
line = "第一章第 一节"
# .* 表示任意匹配除换行符（\n、\r）之外的任何单个或多个字符
matchObj = re.match( r'第(.*)章(.*?) (.*)', line, re.M|re.I) # 灵性的空格
# matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)
 
if matchObj:
   print ("matchObj.group() : ", matchObj.group())
   print ("matchObj.group(1) : ", matchObj.group(1))
   print ("matchObj.group(2) : ", matchObj.group(2))
   print ("matchObj.group(2) : ", matchObj.group(3))
else:
   print ("No match!!")