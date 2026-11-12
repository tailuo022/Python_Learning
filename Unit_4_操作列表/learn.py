names = ["Alice", "Bob", "Charlie", "David"]
for name in names:
    print(f"Hello, {name}, welcome to the party!")
    print("We hope you have a great time!\n")
print("Party over!")
# Python 函数用缩进表示代码块，代码块是函数体，函数体是函数的具体实现
# Python 根据缩进来判断代码行与程序其他部分的关系
# answer
# Hello, Alice, welcome to the party!
# We hope you have a great time!

# Hello, Bob, welcome to the party!
# We hope you have a great time!

# Hello, Charlie, welcome to the party!
# We hope you have a great time!

# Hello, David, welcome to the party!
# We hope you have a great time!

# Party over!
# Thank you for coming!


for value in range(0, 5):
    print(value)
# range(start, stop, step) 输入的参数是整数，输出的是一个整数序列
# start 是序列的起始值，stop 是序列的结束值，step 是序列的步长
# range() 函数默认的步长是 1，如果省略 step 参数，步长就是 1
# range() 函数的输出是一个整数序列，序列的起始值是 start，结束值是 stop - 1
# range(stop) 等价于 range(0, stop)


numbers = list(range(1, 5))
print(numbers)
# list() 函数可以将 range() 函数的输出转换为列表

for value in range(1, 31):
    print(f"{value} 的平方是 {value ** 2}")
# 1 的平方是 1
# 2 的平方是 4
# 3 的平方是 9
# 4 的平方是 16
# 5 的平方是 25
# 6 的平方是 36
# 7 的平方是 49
# 8 的平方是 64
# 9 的平方是 81
# 10 的平方是 100
# 11 的平方是 121
# 12 的平方是 144
# 13 的平方是 169
# 14 的平方是 196
# 15 的平方是 225
# 16 的平方是 256
# 17 的平方是 289
# 18 的平方是 324
# 19 的平方是 361
# 20 的平方是 400
# 21 的平方是 441
# 22 的平方是 484
# 23 的平方是 529
# 24 的平方是 576
# 25 的平方是 625
# 26 的平方是 676
# 27 的平方是 729
# 28 的平方是 784
# 29 的平方是 841
# 30 的平方是 900


squares = []
for value in range(1, 31):
    squares.append(value ** 2)
print(squares)
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900]


min_number = min(squares)
max_number = max(squares)
sum_number = sum(squares)
print(f"最小值是 {min_number}")
print(f"最大值是 {max_number}")
print(f"和是 {sum_number}")
print(f"平均值是 {sum_number / len(squares)}")
# 最小值是 1
# 最大值是 900
# 和是 9455
# 平均值是 315.1666666666667


squares = [values ** 2 for values in range(1, 11)]
print(squares)
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# 列表推导式可以快速生成列表
# 列表推导式的语法是 [expression for item in iterable]
# expression 是要生成的元素，item 是要遍历的可迭代对象
# 可以使用 if 语句来过滤元素
# 例如，要生成一个列表，列表中只包含偶数的平方，可以使用以下代码：
# squares = [values ** 2 for values in range(1, 11) if values % 2 == 0]
# print(squares)
#[4, 16, 36, 64, 100]


print(squares[0:4])
# [1, 4, 9, 16]
# 切片可以获取列表的子序列
# 切片的语法是 [start:stop:step]
# start 是切片的起始值，stop 是切片的结束值，step 是切片的步长
# 如果省略 start 参数，默认的起始值是 0
# 如果省略 stop 参数，默认的结束值是列表的长度
# 如果省略 step 参数，默认的步长是 1
# 例如，要获取列表的前 4 个元素，可以使用以下代码：
print(squares[-4:])
# [81, 100, 121, 144]


for square in squares[0:4]:
    print(square)
# 1
# 4
# 9
# 16


num = squares
print(num)
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
num = squares[:]
print(num)
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
num = squares[2:7]
print(num)
# [9, 16, 25, 36, 49]
# 赋值意味着将一个列表的引用赋值给另一个变量，两个变量指向同一个列表
# 如果对一个变量进行修改，另一个变量也会被修改
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = a
print(a)
print(b)
b[0] = 100
print(b)
print(a)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# [100, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# [100, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a[0] = 1
c = a[:]
print(a)
print(c)
c[0] = 1000
print(c)
print(a)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# [1000, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 切片后修改，原始数据不会被修改


demo = 1, 3
print(demo)
# (1, 3)
# 元祖是不可变的，不能修改
# 如果要修改元祖中的元素，只能创建一个新的元祖
# () 表示元祖 ，[] 表示列表 ，{} 表示字典 
# 元祖的元素可以是任意类型，包括列表、元祖、字典等
# 元祖的元素可以是多个，也可以是一个


demos = (1, 2, 3)
print(demos)
demos_2 = demos
demos_2 = (4, 5, 6)
print(demos_2)
demos = (7, 8, 9)
print(demos)
# (1, 2, 3)
# (4, 5, 6)
# (7, 8, 9)
# 虽然元祖是不可变的，但是赋值可以改变元祖的引用


demo_1 = (1, 2, 3)
demo_2 = (4, 5, 6)
demo_2 = demo_1
print(demo_2)
demo_2 = (7, 8, 9)
print(demo_2)
demo_1 = (1, 2, 4)
print(demo_1)
# (1, 2, 3)
# (7, 8, 9)
# (1, 2, 4)
# 元祖之间可以赋值，赋值后可以修改元祖的引用，但是不能修改元祖中的元素


