#
# @author xiashuo
# @date 2023/6/6 10:59
#

print("------------------------------初始化----------------------------------")
# 空列表
list_empty = []
print(list_empty)
# 直接通过方法创建一个
list_empty_1 = list()
print(list_empty_1)

list0 = ["baidu", "alli"]
print(list0)
# 列表中的元素可以是不同的类型
list_now = ['a', 'b', 'c', 'd', 'e', 'f', 1, 2, 3, 4, 5, 6, 7, 8, 9, True, False]
print(list_now)
# 列表的元素的类型可以是列表，元组，字典，集合
list_nested = ['a', ['b', 'c', 'd'], ('e', 'f'), {"name": 1, "age": 2}, {3, 4, 5, 6, 7, 8}, 9]
print(list_nested)
# 输出 <class 'list'>
print(type(list_nested))

print("------------------------------读取元素/子列表----------------------------------")
# 通过索引访问元素，第一个元素下表为0
print(list_now[0])
print(list_now[2])
# 从后向前访问元素，最后一个元素为-1
print(list_now[-1])
print(list_now[-2])
# 嵌套列表
print(list_nested[1][2])

# 截取列表中的元素返回一个新的list
# 包含左边界，不包含右边界
print(list_now[1:2])
print(list_now[1:-2])
# 指定步长为2
# 结果的索引从0开始，然后是2，然后是4，以此类推
print("步长为2", list_now[::2])
# 左右边界可以不写，
# 左边界不写默认从第一个元素开始
print(list_now[1:])
# 右边界不写默认到最后一个元素
print(list_now[:-2])
# 左右都不写，那就是整个列表
print(list_now[:])
# 当步长大于0的时候左边界必须小于右边界，否则输出空列表
# 输出不为空
print(list_now[-2:-1])
# 输出为空
print(list_now[-1:-2])
# 当步长小于0的时候左边界必须大于右边界，否则输出空列表
# 输出不为空
print(list_now[3:1:-1])
# 输出为空
print(list_now[1:3:-1])

# 列表的倒序操作，跟reverse方法一样
print(list_now)
print(list_now[::-1])

# 注意，对截取出来的列表的更新不会影响原来的列表
sub_list = list_now[0:3]
sub_list[1] = "aaaaa"
print(sub_list)
print(list_now)
# 如果元素是对象或者列表，而对对象属或者列表性进行更新，是会同步到原来的列表中的
list_nested_new = list_nested[0:3]
list_nested_new[1][1] = "&&&&&&"
print(list_nested_new)
print(list_nested)

# 切片操作是可以连写的，灵活使用的话会非常方便
print(list_now[:6][::-1][2:])

print("------------------------------列表元素的增删改查----------------------------------")
# 添加元素
list_now.append(45.12)
print(list_now)

# 在指定位置添加元素
list_now.insert(1, '&&')
print(list_now)

# 直接在列表的末尾追加另一个列表
list_append = ["**", "/", "^^"]
list_now.extend(list_append)
print(list_now)

# extend 可以接受其他的数据容器，比如元组，集合，字典
list_now.extend(("111", "222", "333"))
print(list_now)
# 会将字典的key添加到列表中
list_now.extend({"a1": "111", "b2": "222", "c2": "333"})
print(list_now)
list_now.extend({"qq", "ee", "ff"})
print(list_now)

# 设置指定位置的元素
list_now[1] = "ab"
print(list_now)

# 获取指定元素的下标
print(list_now.index(45.12))
# 如果元素在列表中不存在，会报错
# ValueError: 100 is not in list_now
# print(list_now.index(100))

# 删除第一个匹配的元素
list_now.remove(45.12)
print(list_now)
# 如果元素不存在， remove方法会报错
# ValueError: list_now.remove(x): x not in list_now
# list_now.remove(45.12)
# print(list_now)

# 删除最后一个元素并返回
print(list_now.pop())
print(list_now)
# 也可以指定索引删除元素并返回，类似于remove
print(list_now.pop(-2))
print(list_now)

# 也可以用 del 命令删除指定索引的元素
del list_now[-1]
print(list_now)

# 统计某个元素在列表中出现的次数，比如 9 这个元素
print(list_now.count(9))

print("------------------------------对列表的整体操作----------------------------------")
# 列表长度
print(len(list_now))

list_int = [12, 45, 78]
print(max(list_int))
print(min(list_int))
# max 和 min 只能对所有元素类型相同的list进行运算，sort方法也是，否则会报错

# 列表的复制
# 浅复制，不是深复制
list_copy = list_now.copy()
print(list_copy)
# 对复制出来的列表的指定索引的更新，不会同步到原来的列表
list_copy[0] = 999
print(list_copy)
print(list_now)
# 如果元素是对象或者列表，而对对象属性或者列表进行更新，是会同步到原列表中的
list_nested_copy = list_nested.copy()
list_nested_copy[1][1] = "******"
print(list_nested_copy)
print(list_nested)

# 将list倒序，也可以直接通过 [::-1] 实现
list_now.reverse()
print(list_now)
list_now.reverse()

# 清除列表中的所有元素
list_now.clear()
print(list_now)

print("------------------------------列表元素的排序----------------------------------")
# sort 只能对所有元素类型相同的list进行运算，max 和 min 方法也是，否则会报错
# 对列表中的元素进行排序
list_num = [12.12, 78, 1, 5, 6, 3]
print(list_num)
# 默认升序
list_num.sort()
print(list_num)
# 倒叙
list_num.sort(reverse=True)
print(list_num)


# 自定义排序规则
# 根据字符串长度
def strLen(elem):
    return len(elem)


str_list = ['aaaaaa', 'aa', 'aaa', 'aaaaaaaaaaaaaaa', 'aaaaaaaaa']
str_list.sort(key=strLen, reverse=False)
print(str_list)

print("------------------------------对列表的符号操作，非常方便----------------------------------")
list_new = ["aaa", "bbb", "ccc", "ddd"]
list_2_plus = ["1111", "222", "333", "444", "555"]
# 可以直接通过 + 将两个列表合并，类似于 extend 方法
plus = list_new + list_2_plus
print(plus)
# 原列表不会受影响
print(list_new)

# 通过 *n 将列表的元素复制n倍
multiple = list_new * 4
print(multiple)
# 原列表不会受影响
print(list_new)

# 直接通过 in 语句判断元素是否在列表中，类似于 index 方法
print(3 in list_new)
print("aaa" in list_new)
# not in 判断元素是否不在列表中
print("aaa" not in list_new)

# for-in 循环遍历list
for i in list_new:
    print(i, end=' ')
print()
print(list_new)

print("------------------------------列表推导式----------------------------------")

list_exp = [x + 2 for x in range(0, 10) if x < 6]
# 输出 [2, 3, 4, 5, 6, 7]
print(list_exp)

print("------------------------------列表的比较----------------------------------")

# 导入 operator 模块
import operator

a = [1, 2]
b = [2, 3]
c = [2, 3]
print("operator.eq(a,b): ", operator.eq(a, b))
print("operator.eq(c,b): ", operator.eq(c, b))

# 复杂列表
str_list_0 = ['aaa', 'bb', 'cccccc', 'dd']
str_list_0_copy = ['aaa', 'bb', 'cccccc', 'dd']
str_list_1 = ['aaa', 'cccccc', 'dd', 'bb']
print(operator.eq(str_list_0, str_list_0_copy))
print(operator.eq(str_list_0, str_list_1))
# 元素类型为列表的列表
list_ele_list_0 = [['aaa'], ['111'], ['222']]
list_ele_list_1 = list_ele_list_0.copy()
print(list_ele_list_1)
print(operator.eq(list_ele_list_0, list_ele_list_1))

print("------------------------------将别的容器对象转化为列表----------------------------------")
# 从字符串转化而来
list_from_str = list("abcdefghijklmnopqrstuvwxyz")
print(list_from_str)
# 从元组转化而来
list_from_tuple = list((12, 23.45))
print(list_from_tuple)
# 从集合转化而来
list_from_set = list({12, 23.45})
print(list_from_set)
# 从字典转换而来 获取key转化为列表
list_from_dict = list({"name": "12", "age": "23.45"})
print(list_from_dict)
