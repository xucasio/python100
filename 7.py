# 将一个列表的数据复制到另一个列表中
import copy
list1 = [1, 2, 34, 5, 6]
# list2 = list1 // 测试引用会受影响，深拷贝
list4 = [{'id': 1, 'name': 'xu'}, {'id': 3, 'name': 'chen'}]
list2 = list1.copy()
# 这个是重点
list3 = copy.deepcopy(list4)
list3[0]['name'] = 'li'
list2.append(12)
# range从0开始到len刚好是一个数组的遍历
# for i in range(0, len(list1)):
#     list2.append(list1[i])
print('list1', list1)
print('list2', list2)
print('list3', list3)
print('list4', list4)
