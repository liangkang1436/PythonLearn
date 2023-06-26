#
# @author xiashuo
# @date 2023/6/4 17:09
#


name = "xiashuo.xyz"
# 循环字符串中的字符
for i in name:
    print(f"{i}", end='')
print("-------")

# 通过range可以获取一个简单的数字序列
# 从0(包含)开始到10(不包含)
# 注意，变量类型是 <class 'range'>
print(type(range(0, 10)))
# for循环
for i in range(10):
    print(f"{i}")
print("-------")
# 从5(包含)开始到10(不包含)
for i in range(5, 10):
    print(f"{i}")
print("-------")
# 从5(包含)开始到10(不包含)，设置序列的步长（step）为2，即每隔2输出一个数字，默认的step是1
for i in range(5, 10, 2):
    print(f"{i}")
print("-------")

# 如何获取被便利元素的索引呢？用 enumerate 方法即可
for inx, val in enumerate(name):
    print(f"{inx}处的元素是{val}")

# 从 3 到20，每隔5个数字输出一次
for index, ele in enumerate(range(3, 20, 5)):
    print(f"{index}: {ele}")
# 注意，在for循环的外部，访问index和ele，是可以访问到的，这一点跟Java很不一样
# 这样是违反规范的，不建议这样做
# 可以看到爆黄色警告
print(f"在for循环的外部访问for循环的内部的临时变量：{index}: {ele}")
# 如果你确实需要在for循环的外部来访问，你可以先把for循环内部需要用到的变量定义好，然后就for循环的时候会直接使用这些变量
index_new = 0
ele_new = 0
# for循环会直接使用
for index_new, ele_new in enumerate(range(3, 20, 5)):
    print(f"{index_new}: {ele_new}")
print(f"在for循环的外部访问变量：{index_new}: {ele_new}")

# 九九乘法表 for循环版本
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{i}*{j}={i * j}\t", end="")
    print()
print("输出结束")

print("------------------------------for 的特别用法----------------------------------")

print("------------------- for 输出多个值 -------------------")
# 基于Python的自动解包特性，for 循环有一个很有意思的特性， 即
# 如果被迭代的序列的元素本身也可以迭代，则可以使用多个对象来承接，而如果被迭代的序列的元素无法迭代，但是你用多个对象承接，则会报错

# 用单个对象承接 字符串
list_for = ["aa", "bb", "cc", "dd"]
for item in list_for:
    print(item, end=" ")
print()

# 因为 字符串本身是字符的序列，可以迭代，因此可以用多个对象承接，同时承接的变量的数量必须与元素中可迭代的数量相同
# 会尝试迭代序列（列表，元组，集合，字典）的每一个元素，然后顺序赋值给声明的变量，比如char1, char2
# 输出 a-b c-d e-f g-h
list_for_2 = ["ab", "cd", "ef", "gh"]
for char1, char2 in list_for_2:
    print(f"{char1}-{char2}", end=" ")
print()

# 如果序列的元素本身（是数字或者Boolean，而不是字符串、列表元组，集合，字典），无法迭代，则会报错
# TypeError: cannot unpack non-iterable int object
# list_for_3 = [12, 34, 56, 78]
# for num1, num2 in list_for_3:
#     print(f"{num1}-{num2}", end=" ")
# print()

# 如果可迭代的对象的每个可迭代的元素的长度是四，但是你只声明了两个接收的值，那么依然会报错，此时，你可以在变量前面加* ，加*的变量会变成一个列表
# 因为结果是集合，是无序的，所以输出结果不是确定的
list_for_3 = {"a12", "b45", "c78", "d89"}
for index_3, *val_3 in list_for_3:
    print(f"{index_3}-{val_3}", end=" ")
print()

print("------------------- for 输入多个值 -------------------")
# 通过zip函数，zip函数的结果类型是zip
# 通过zip函数我们可以将多个序列中相同索引的元素放到一个元组中，然后将所有的元组组成列表返回，返回的列表的长度将由长度最小的序列决定
# 有了这个方法，我们就可以在一次循环中处理多个序列的数据，真的非常方便，这在Java里面也是没有的
# 混合三个序列
list_a = [1, 2, 3]
list_b = ["a", "b", "c"]
tuple_c = True, False
result = zip(list_a, list_b, tuple_c)
# 结果类型为 zip
print(result, type(result))
for a, b, c, in result:
    print(a, b, c)
# 输出
# 1 a True
# 2 b False
