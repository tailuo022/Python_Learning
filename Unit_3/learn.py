number = [1, 2, 3, 4, 5]
first_name = ['zhao', 'qian', 'sun', 'li', 'zhou']
print(number)
print(number[0])
print(number[-1])
print(f"The first name is: {first_name[3].title()}")
# [1, 2, 3, 4, 5]
# 1
# 5
# The first name is: Li


# 修改
number[0] = 0
print(number)
# [0, 2, 3, 4, 5]


# 增加
number.append(6)
print(number)
# [0, 2, 3, 4, 5, 6]
# .append() 方法用于在列表末尾添加新的元素。
number.insert(0, -1)
print(number)
# [-1, 0, 2, 3, 4, 5, 6]
# .insert( 索引，元素 ) 方法用于在列表的指定位置添加新的元素。


# 删除
del number[3]
print(number)
# [-1, 0, 2, 4, 5, 6]
# del 语句用于删除列表中的元素。
new_number = number.pop()
print(new_number)
print(number)
# 6
# [-1, 0, 2, 4, 5]
# pop() 方法用于删除列表末尾的元素，并返回该元素的值。
another_number = number.pop(2)
print(another_number)
print(number)
# 2
# [-1, 0, 4, 5]
# .pop( 索引 ) 方法用于删除列表中指定位置的元素，并返回该元素的值。
number.remove(4)
print(number)
# [-1, 0, 5]
# .remove( 元素 ) 方法用于删除列表中指定的元素。


# 永久排序
number = [0, 3, 1, 4, 2, 5]
number.sort()
print(number)
# [0, 1, 2, 3, 4, 5]
# .sort() 方法用于对列表进行排序。
number.sort(reverse=True)
print(number)
# [5, 4, 3, 2, 1, 0]
# .sort(reverse=True) 方法用于对列表进行逆序排序。


# 临时排序
number = [0, 3, 1, 4, 2, 5]
print(f"Here is the original list: {number}")
sorted_number = sorted(number)
print(f"Here is the sorted list: {sorted_number}")
print(f"Here is the original list again: {number}")
print(f"Here is the original list: {sorted(number, reverse=True)}")
# Here is the original list: [0, 3, 1, 4, 2, 5]
# Here is the sorted list: [0, 1, 2, 3, 4, 5]
# Here is the original list again: [0, 3, 1, 4, 2, 5]
# Here is the original list in reverse order: [5, 4, 3, 2, 1, 0]
# sorted() 函数用于对列表进行临时排序，不会修改原列表。
# sorted( 列表, reverse=True ) 函数用于对列表进行临时逆序排序，不会修改原列表。


# 反转列表
number = [0, 3, 1, 4, 2, 5]
number.reverse()
print(number)
# [5, 2, 4, 1, 3, 0]
# .reverse() 方法用于反转列表中的元素顺序。


# 获取列表长度
number = [0, 3, 1, 4, 2, 5]
length = len(number)
print(f"The length of the list is: {length}")
# The length of the list is: 6
# len() 函数用于获取列表的长度，即列表中元素的个数。