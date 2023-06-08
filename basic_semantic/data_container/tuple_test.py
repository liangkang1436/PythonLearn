#
# @author xiashuo
# @date 2023/6/7 11:28
#

print("------------------------------初始化----------------------------------")
# 空元组
tuple0 = ()
print(tuple0, type(tuple0))
# 直接通过方法创建一个
tuple1 = tuple()
print(tuple1, type(tuple1))

# 只有一个元素的时候，在这个元素后面要加上一个逗号，不加的话整体不会被识别为元组，而是运算符
tuple_single = (50)
# 50 <class 'int'>
print(tuple_single, type(tuple_single))
# 下面这样才是元组
tuple_single_new = (50,)
# (50,) <class 'tuple'>
print(tuple_single_new, type(tuple_single_new))

tuple3 = ("baidu", "alli")
print(tuple3)
# 元组中的元素可以是不同的类型
tuple_now = ('a', 'b', 'c', 'd', 'e', 'f', 1, 2, 3, 4, 5, 6, 7, 8, 9, True, False)
print(tuple_now)
# 元组的元素的类型可以是列表，元组，字典，集合
tuple_nested = ('a', ['b', 'c', 'd'], ('e', 'f'), {"name": 1, "age": 2}, {3, 4, 5, 6, 7, 8}, 9)
print(tuple_nested)
# 输出 <class 'tuple'>
print(type(tuple_nested))

# 元组声明的时候，可以把括号去掉，这一点很重要，当我们看到用一个变量等于逗号分割开的一系列元素的时候，这个变量其实是元组
tuple_simple = 'a', 'b', 'c', 1, 2, 3, False,
print(tuple_simple)
# 单个元素的元组元素末尾得加上一个逗号
tuple_simplest = 12,
# (12,) <class 'tuple'>
print(tuple_simplest, type(tuple_simplest))

print("------------------------------读取元素/子元组----------------------------------")
# 通过索引访问元素，第一个元素下表为0
print(tuple_now[0])
print(tuple_now[2])
# 从后向前访问元素，最后一个元素为-1
print(tuple_now[-1])
print(tuple_now[-2])
# 嵌套元组
print(tuple_nested[2][1])

# 截取元组中的元素返回一个新的tuple
# 包含左边界，不包含右边界
print(tuple_now[1:2])
print(tuple_now[1:-2])
# 左右边界可以不写，
# 左边界不写默认从第一个元素开始
print(tuple_now[1:])
# 右边界不写默认到最后一个元素
print(tuple_now[:-2])
# 左右都不写，那就是整个元组
print(tuple_now[:])
# 左边界必须在右边界的左边，否则输出空元组
print(tuple_now[-1:-2])

print("------------------------------元组元素的增删改查----------------------------------")

# tuple_now[1] = "aaaaa"
# # 报错，元组中的指定索引的元素不允许更新
# # 'tuple' object does not support item assignment
# print(tuple_now)
# 同时也不允许增加元素
# 同时也不允许删除元组中的元素，也就是说整个元组一旦初始化，就动都不能动了
# 但是有一个特例，就是如果元组的元素的类型是列表或者其他对象，那我们是可以修改对象的属性的
# 这就有点像Java中final关键字的效果

print(tuple_nested)
tuple_nested[1][0] = "+"
tuple_nested[1][1] = "-"
tuple_nested[1][2] = "&&"
print(tuple_nested)

# 但是依然不能修改类型为元组类型的元素
# tuple_nested[2][1] = "***"

# 但是我们可以删除整个元组
tuple_del = 12, 45, 78
print(tuple_del)
del tuple_del
# name 'tuple_del' is not defined.
# print(tuple_del)

# 获取指定元素的下标
print(tuple_now.index(9))
# 如果元素在元组中不存在，会报错
# ValueError: 100 is not in tuple_now
# print(tuple_now.index(100))

# 统计某个元素在元组中出现的次数，比如 1 这个元素
# 返回2 因为True也算1
print(tuple_now.count(1))
# 返回1 因为False也算0
print(tuple_now.count(0))

print("------------------------------对元组的整体操作----------------------------------")
# 元组长度
print(len(tuple_now))

tuple_int = (12, 45, 78, 754)
print(max(tuple_int))
print(min(tuple_int))

# max 和 min 只能对所有元素类型相同的tuple进行运算，否则会报错
# tuple_mix = (12, 45, 78, 754,"sdfasd")
# # '>' not supported between instances of 'str' and 'int'
# print(max(tuple_mix))


print("------------------------------对元组的符号操作，非常方便----------------------------------")
tuple_new = ("aaa", "bbb", "ccc", "ddd")
tuple_2_plus = ("1111", "222", "333", "444", "555")
# 可以直接通过 + 将两个元组合并
plus = tuple_new + tuple_2_plus
print(plus)
# 原元组不会受影响
print(tuple_new)

# 通过 *n 将元组的元素复制n倍
multiple = tuple_new * 4
print(multiple)
# 原元组不会受影响
print(tuple_new)

# 直接通过 in 语句判断元素是否在元组中，类似于 index 方法
print(3 in tuple_new)
print("aaa" in tuple_new)
# not in 判断元素是否不在元组中
print("aaa" not in tuple_new)

# for-in 循环遍历tuple
for i in tuple_new:
    print(i, end=' ')
print()
print(tuple_new)

print("------------------------------元组的比较----------------------------------")

# 导入 operator 模块
import operator

a = (1, 2)
b = (2, 3)
c = (2, 3)
print("operator.eq(a,b): ", operator.eq(a, b))
print("operator.eq(c,b): ", operator.eq(c, b))

# 复杂元组
str_tuple_0 = ('aaa', 'bb', 'cccccc', 'dd')
str_tuple_0_copy = ('aaa', 'bb', 'cccccc', 'dd')
str_tuple_1 = ('aaa', 'cccccc', 'dd', 'bb')
print(operator.eq(str_tuple_0, str_tuple_0_copy))
print(operator.eq(str_tuple_0, str_tuple_1))
# 元素类型为元组的元组
tuple_ele_tuple_0 = (('aaa'), ('111'), ('222'))
tuple_ele_tuple_1 = (('aaa'), ('111'), ('222'))
print(operator.eq(tuple_ele_tuple_0, tuple_ele_tuple_1))

print("------------------------------将别的序列转化为元组----------------------------------")
# 从元组转化而来
tuple_from_list = tuple([12, 23.45])
print(tuple_from_list)
tuple_from_set = tuple({12, 23.45})
print(tuple_from_set)
# 获取key转化为元组
tuple_from_dict = tuple({"name": "12", "age": "23.45"})
print(tuple_from_dict)
