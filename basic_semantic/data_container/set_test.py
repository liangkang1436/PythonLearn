#
# @author xiashuo
# @date 2023/6/12 20:17
#


print("------------------------------初始化----------------------------------")

# 空集合
set_empty = {}
# 输出{} <class 'dict'>，字典类型，而不是集合类型
print(set_empty, type(set_empty))
# 这样才是空集合
set_empty = set()
# 输出set() <class 'set'>
print(set_empty, type(set_empty))

set_example = {"a", "a", "a", "a", "a", "a"}
# 只会输出 {'a'}，说明其自动去充了
print(set_example)
set_example_2 = set(["b", "b", "b", "b", "b", "b"])
# 只会输出 {'b'}，说明set方法将列表中的元素自动去重了
print(set_example_2)

# 集合中的元素可以是不同的类型
set_now = {'a', 'b', 'c', 'd', 'e', 'f', 1, 2, 3, 4, 5, 6, 7, 8, 9, True, False}
# set 是一个无序的集合，不会按照元素声明的顺序保存元素
print(set_now)
# 集合的元素的类型可以是元组，但是不能是列表，字典，集合
# 如果元组的元素的顺序不一样，也会被视为不同的元素保留在集合中
set_nested = {'a', ('e', 'f'), ('f', 'e'), 9, 10}
# 输出 {('e', 'f'), 9, 10, 'a', ('f', 'e')}
print(set_nested)
# 输出 <class 'set'>
print(type(set_nested))

print("------------------------------读取元素/子集合----------------------------------")
# 报错：TypeError: 'set' object is not subscriptable
# 集合无法通过下标访问
# print(set_now[1])
print("集合无法通过下标访问")

print("------------------------------集合元素的增删改查----------------------------------")
# 添加元素
# add 方法只能添加一个元素，如果元素已经存在了，则啥也不干，不存在，则添加到集合中
set_now.add(1)
print(set_now)
set_now.add(10)
print(set_now)
# add 方法传入一个元组，不会出现元组中的元素跟集合中现有元素取并集的效果，而是直接将元组整体作为一个元素添加到集合中，想要实现这样的效果应该使用update方法
# add 方法无法添加列表、字典、集合作为集合中的元素，这个在前面初始化集合的时候就已经学习过了
set_now.add((1, 2))
print(set_now)
# update方法可传入多个容器对象（可传入多个参数），然后会自动将这些容器对象中的元素与集合中的元素进行取并集的操作（效果等同于 | 操作符和 union 方法）
# 字典会使用key，不使用value
# 很明显，update方法更加方便实用
set_now.update(["aa", "bb", "cc"], (1, 2, 3, 11, 12), {"a1", "b1", "c1"}, {"A1": 94, "B1": 98, "C1": 99})
print(set_now)

# 删除匹配的元素
set_now.remove(12)
print(set_now)
# 删除元组
set_now.remove((1, 2))
print(set_now)
# 如果元素不存在， remove方法会报错
# KeyError: 112
# set_now.remove(112)
# print(set_now)

# 移除匹配的元素，如果这个元素不在集合中，那就啥也不做
# 很明显，discard 更好用
set_now.discard(112)

# 随机删除集合中的一个元素，如果集合是空的，那就会报错
# pop 方法会对集合进行无序的排列，然后将这个无序排列集合的左面第一个元素进行删除。
print(set_now.pop())
print(set_now)

print("------------------------------对集合的整体操作----------------------------------")
# 集合长度
print(len(set_now))

set_int = [12, 45, 78]
print(max(set_int))
print(min(set_int))
# max 和 min 只能对所有元素类型相同的set进行运算，否则会报错

# 集合的复制
# 浅复制，不是深复制
# 如果元素是对象或者集合，而对对象属性或者集合进行更新，是会同步到原集合中的
set_copy = set_now.copy()
print("原始set", set_now)
print("复制set", set_copy)

# 清除集合中的所有元素
set_now.clear()
print(set_now)

print("------------------------------集合元素的排序----------------------------------")


# 自定义排序规则
# 根据元素长度
def eleLen(elem):
    # 相当于一个hash操作
    # 返回值越大，升序排序的时候就越靠后
    if type(elem) == bool:
        return 1
    elif type(elem) == int:
        return len(str(elem))
    else:
        # 剩下的都是容器了
        return len(elem)


# 容器通用排序操作，返回一个新的列表，原字典是不变的，
# 集合中的元素的类型是不限定的，因此得定制key函数，否则无法比较，只能返回空列表
sorted_list = sorted(set_copy, key=eleLen, reverse=False)
print(set_copy)
print(sorted_list)

print("------------------------------对集合的符号操作，非常方便----------------------------------")
# 集合不支持 + 操作
# 集合不支持 * 操作

# 注意，以下操作符都不会修改原集合，而是返回一个新的集合
# a - b  集合a中包含而集合b中不包含的元素，类似于 difference 方法
# a | b  集合a或b中包含的所有元素，类似于 union 方法
# a & b  集合a和b中都包含了的元素，类似于 intersection 方法
# a ^ b  不同时包含于a和b的元素，类似于 symmetric_difference 方法

set_1 = {"aaa", "bbb", "ccc", "ddd", "1111", "222"}
set_2 = {"1111", "222", "333", "444", "555"}
# set_1 中删除 set_2 中的元素
print(set_1 - set_2)
# set_1 set_2 取并集
print(set_1 | set_2)
# set_1 set_2 取交集
print(set_1 & set_2)
# set_1 set_2 的并集去掉 set_1 set_2 的交集
print(set_1 ^ set_2)
# 等于
print((set_1 | set_2) - (set_1 & set_2))
# 可以通过 - 快速地去除一个元素
print(set_1 - {"aaa"})

# 直接通过 in 语句判断元素是否在集合中，类似于 index 方法
print(3 in set_1)
print("aaa" in set_1)
# not in 判断元素是否不在集合中
print("aaa" not in set_1)

# for-in 循环遍历set
# 乱序输出
for i in set_1:
    print(i, end=' ')
print()
print(set_1)

print("------------------------------集合推导式操作----------------------------------")
set_exp = {x for x in 'abracadabra' if x not in 'abc'}
print(set_exp)

print("------------------------------集合的比较----------------------------------")

# 导入 operator 模块
import operator

a = {1, 2}
b = {2, 1}
c = (2, 3)
# True
print("operator.eq(a,b): ", operator.eq(a, b))
# False
print("operator.eq(c,b): ", operator.eq(c, b))

print("------------------------------集合的相关方法----------------------------------")

set_3 = {"a1", "b1", "c1"}
set_4 = {"a1", "a2", "a3"}
set_5 = {"1", "2", "3"}
set_6 = {"1", "2"}
set_7 = {"2", "3", "4", "5"}

# 取并集，效果等同于 | 操作符
print(set_3.union(set_4))

# 集合关系的判断
# 两个集合是否没有交集
print(set_3.isdisjoint(set_4))
print(set_3.isdisjoint(set_5))
# 当前集合是否是传入的集合的子集
print(set_6.issubset(set_5))
# 当前集合是否是传入的集合的父集
print(set_5.issuperset(set_6))

# 在当前集合中，但是不在传入的集合中的，可传入多个集合，类似 - 操作符
# 但是返回的是一个新的集合，原集合是不受影响的
print(set_5.difference(set_6))
print(set_5)
# 原集合会受影响，要谨慎使用
# 此方法返回None
print(set_5.difference_update(set_6))
print(set_5)

# 取交集，类似 & 操作符
print(set_3.intersection(set_4))
set_3.intersection_update(set_4)
print(set_3)

# 返回两个集合中所有只存在于一个集合中的元素，类似 ^ 操作符
print(set_6.symmetric_difference(set_7))
set_6.symmetric_difference_update(set_7)
print(set_6)

print("------------------------------将别的容器对象转化为集合----------------------------------")
# 从字符串转化而来
set_from_str = set("abcdefghijklmnopqrstuvwxyz")
print(set_from_str)
# 从列表转化而来
set_from_list = set([12, 23.45])
print(set_from_list)
# 从元组转化而来
set_from_tuple = set((12, 23.45))
print(set_from_tuple)
# 从字典转换而来 获取key转化为列表
set_from_dict = set({"name": "12", "age": "23.45"})
print(set_from_dict)
