items=[1,2,3,4,5]
lists=[6,7,8,9,10]
datas=[11,12,13,14,15]
cons=[16,17,18,19,20]
# 这种循环好叼
for item,li,data,con in zip(items,lists,datas,cons):
    print(item,li,data,con,sep='\n------------\n')