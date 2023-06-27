#
# @author xiashuo
# @date 2023/6/13 12:41
#

print("------------------------------初始化----------------------------------")

# 空字典
dict_empty = {}
# 输出 {} <class 'dict'>
print(dict_empty, type(dict_empty))
# 直接通过方法创建一个
dict_empty_1 = dict()
print(dict_empty_1)

# 键必须是唯一的，但值则不必。
# 如果key重复，则后面的会覆盖前面的
dict_0 = {"aa": "bb", "aa": "222"}
print(dict_0)
# 键必须是不可变的，如字符串，数字 , Boolean，此外，元组可以作为key，因为元组是不可变的，但是列表、集合、字典是可变的，都不能作为key
# 值可以取任何数据类型，可以是任何的 python 对象，既可以是标准的对象，也可以是用户定义的
dict_1 = {"aa": "bb", ("aaa", "bb"): "1212", True: 12}
print(dict_1)
# TypeError: unhashable type: 'list'
# dict_2 = {"aa":"bb",["aaa","bb"]:"1212"}
# print(dict_2)
# TypeError: unhashable type: 'set'
# dict_3 = {"aa":"bb",{"aaa","bb"}:"1212"}
# print(dict_3)
# TypeError: unhashable type: 'dict'
# dict_4 = {"aa":"bb",{"aaa":"aa","bb":"bb"}:"1212"}
# print(dict_4)
# value 可以是字符串，数字，列表，元组，集合，字典，并且可以继续嵌套下去
# 字典完美契合JSON的格式
dict_5 = {"aa": "bb", "bb": [12, 23, 14], "cc": (12, 23, 14), "dd": {12, 23, 14},
          "ee": {12: "aaa", 23: "bbb", 14: "ccc"}}
print(dict_5)

dict_now = {"aa": "a1", "bb": [11, 12, 13], "cc": (21, 22, 23), "dd": {31, 32, 33},
            "ee": {41: "e1", 42: "e2", 43: "e3"}}

# 创建一个新字典，以可迭代对象的所有值为key，然后指定一个初始化，如果不指定的话就为null
# 输出 {1: 99, 2: 99, 3: 99, 4: 99}
new_dict = dict.fromkeys([1, 2, 3, 4], 99)
print(new_dict)

print("------------------------------读取元素/子字典----------------------------------")
print("字典无法通过下标索引访问，只能通过key访问")

# 直接通过下标访问
print(dict_now["aa"])
print(dict_now["bb"][1:])
print(dict_now["ee"][42])
# 如果用字典里没有的键访问数据，会报错
# KeyError: 'ff'
# print(dict_now["ff"])

# 获取指定key的val，比通过下标访问好多了
a_val = dict_now.get("aa")
print(a_val)
# key不存在，返回 None，不报错
a_val_null = dict_now.get("aab")
print(a_val_null)
# 带默认值的get
ab_val = dict_now.get("aab", "111")
print(ab_val)

# 摘取特定的key组成一个子字典，
# 无法通过下标完成，但是可以通过字典推导式来完成
dict_key = ["aa", "bb", "cc"]
# 写法1
dict_child_1 = {key: value for key, value in dict_now.items() if key in dict_key}
print(dict_child_1)
# 写法2
dict_child_2 = {key: dict_now[key] for key in dict_now if key in dict_key}
print(dict_child_2)
# 写法3  dict_now.keys() & dict_key 这两个集合取并集
dict_child_3 = {key: dict_now[key] for key in dict_now.keys() & dict_key}
print(dict_child_3)

print("------------------------------字典元素的增删改查----------------------------------")

# 使用[] 可更新key对应的val，比 setdefault 好用多了
dict_now["ff"] = 12
print(dict_now)
# 如果key在字典中不存在，则直接添加 key和val，非常方便，比 setdefault 好用多了
dict_now["hh"] = 1111
print(dict_now)

# 如果key在字典中不存在，则插入这个key，你可以指定这个key的val，没指定的话，默认值就是None，最终返回这个key的val
# 如果key在字典中存在，则返回这个key的值，
# 所以这个方法实际上是不能更新指定key的val的，
# 要更新指定key的val，只能用update方法
ret_val = dict_now.setdefault("ff")
# 返回值为 None
print(ret_val)
ret_val_2 = dict_now.setdefault("gg", "g1")
# 返回值为 g1
print(ret_val_2)
# 返回值为 ee对应的val 为 {41: 'e1', 42: 'e2', 43: 'e3'}
ret_val_3 = dict_now.setdefault("ee", "aaa")
print(ret_val_3)
# 字典的 key为ee的val，并没有更新为 aaa，依然是 {41: 'e1', 42: 'e2', 43: 'e3'}
# 所以 setdefault 方法并不能用来更新 key 对应的 val
print(dict_now)

# update方法，有三种参数
# 第一种，直接传入一个字典，只有key在传入的字典中存在的val才会被更新
# 第二种，传入长度为2的可迭代对象的序列，比如[("a",1),("b",2)]，第一项为key，第二项为val，跟第一种参数一样，只有key在传入参数中的val才会更新
# 第三种，直接传入关键字函数,name为字典的key，val为更新的目标值，
# 不能同时传入第一种和第二种参数，第一种/第二种参数 和 第三种参数可以同时生效，且第三种参数后生效，可以覆盖第一种/第二种参数
dict_copy = dict_now.copy()
dict_copy.update({"aa": 1, "bb": 2, "cc": 3})
print(dict_copy)
dict_copy = dict_now.copy()
dict_copy.update([("aa", 100), ("bb", 200), ("cc", 300)])
print(dict_copy)
dict_copy = dict_now.copy()
dict_copy.update(aa=98, bb=998, cc=9998)
print(dict_copy)
# 第一种参数不可以跟第三种参数一起生效
# dict_copy = dict_now.copy()
# dict_copy.update({"aa": 1, "bb": 2, "cc": 3}, [("aa", 100), ("bb", 200), ("cc", 300)])
# print(dict_copy)
# 第一种参数可以跟第三种参数一起生效
dict_copy = dict_now.copy()
dict_copy.update({"aa": "x", "bb": "y", "cc": "z"}, dd=998)
print(dict_copy)
# 第二种参数可以跟第三种参数一起生效
dict_copy = dict_now.copy()
dict_copy.update([("aa", 100), ("bb", 200), ("cc", 300)], dd=998)
print(dict_copy)
# aa 最终为998
dict_copy = dict_now.copy()
dict_copy.update({"aa": "x", "bb": "y", "cc": "z"}, aa=998)
print(dict_copy)

# 删除键 'Name' 不如 pop 方法好用
del dict_now['hh']
print(dict_now)
# 删除一个不存在的key，会报错
# 提示 KeyError: 'hhaa'
# del dict_now['hhaa']
# print(dict_now)

# 删除字典 key（键）所对应的值，返回被删除的值。如果key在字典中不存在，则报错，不过此时你可以指定一个默认值，这样key在字典中不存在就只会返回默认值，而不报错
# 当我们不知道key存不存在的时候，我们可以添加一个默认值，如果返回结果是默认值，则表示key不存在，如果返回结果不是默认值，则说明key存在，且已经删除成功
# 因为字典中存在 gg这个key，所以此时添加默认值也不会返回
val_1 = dict_now.pop("gg")
# 输出 g1
print(val_1)
# 因为 gg 这个key 已经被删除，所以再删一次，此时已经不存在这个key，会报错
# KeyError: 'hh'
# val_2 = dict_now.pop("gg")
# print(val_2)
# 添加默认值，表示key不存在的时候返回默认值
val_3 = dict_now.pop("gg", "aaa")
print(val_3)
print(dict_now)

# 返回并删除字典中的最后一对键和值。并将其作为一个两个元素的元组返回，如果字典为空，则报错
del_pair_tuple = dict_now.popitem()
print(del_pair_tuple)
print(dict_now)

print("------------------------------对字典的整体操作----------------------------------")
# 字典长度
print(len(dict_now))

# 将字典输出为字符串
print(str(dict_now))
# 和直接输出没啥区别
print(dict_now)

# 返回key的最大值和最小值
print(max(dict_now))
print(min(dict_now))

# 字典的复制
# 浅复制，不是深复制
# 如果key的val是对象或者字典，而对对象属性或者字典进行更新，是会同步到原字典中的
dict_copy = dict_now.copy()
print(dict_copy)
# 清空字典
dict_copy.clear()
print(dict_copy)

# 删除字典对象
# 删除之后对象都没了
del dict_copy
# 报错，并提示：name 'dict_copy' is not defined.
# print(dict_copy)


# 将所有的key,val转化为元组并列表，并封装为一个 dict_items 类型的变量，然后返回
# 一般在for循环中，想要直接获取key和val的话，会使用此函数
item_of_dict = dict_now.items()
# 内容为 dict_items([('aa', 'a1'), ('bb', [11, 12, 13]), ('cc', (21, 22, 23)), ('dd', {32, 33, 31}), ('ee', {41: 'e1', 42: 'e2', 43: 'e3'})])
# 类型为 dict_items
print(item_of_dict, type(item_of_dict))
# 将所有的key放到列表中，并封装为一个 dict_keys 类型的变量，然后返回
key_of_dict = dict_now.keys()
# 内容为 dict_keys(['aa', 'bb', 'cc', 'dd', 'ee'])
# 类型为 dict_keys
print(key_of_dict, type(key_of_dict))
# 将所有的val放到列表中，并封装为一个 dict_values 类型的变量，然后返回
val_of_dict = dict_now.values()
# 内容为 dict_values(['a1', [11, 12, 13], (21, 22, 23), {32, 33, 31}, {41: 'e1', 42: 'e2', 43: 'e3'}])
# 类型为 dict_values
print(val_of_dict, type(val_of_dict))

print("------------------------------对字典的符号操作，非常方便----------------------------------")
# 字典不支持 + 操作
# 字典不支持 * 操作

dict_new = {"aaa": 45, "bbb": 60}

# 直接通过 in 语句判断key是否在字典中
print("aaaa" in dict_new)
print("aaa" in dict_new)
# not in 判断元素是否不在字典中
print("aaa" not in dict_new)

# for-in 循环遍历list
for i in dict_new:
    print(i, dict_new[i], end=' ')
print()

# 这样很符合直觉
for k, v in dict_new.items():
    print(k, v, end=' ')
print()

print("------------------------------字典推导式----------------------------------")

# 前面的获取子字典的例子
# 写法1
dict_child_1 = {key: value for key, value in dict_now.items() if key in dict_key}
print(dict_child_1)
# 写法2
dict_child_2 = {key: dict_now[key] for key in dict_now if key in dict_key}
print(dict_child_2)
# 写法3  dict_now.keys() & dict_key 这两个集合取并集
dict_child_3 = {key: dict_now[key] for key in dict_now.keys() & dict_key}
print(dict_child_3)
# 将字典的所有的key加上一个后缀组成一个列表
dict_key_list = [key + "&&" for key in dict_now]
print(dict_key_list)

print("------------------------------ 字典的比较 ----------------------------------")

# 导入 operator 模块
import operator

dict_a = {1: 1, 2: 2}
dict_b = {1: 1, 2: 2}
dict_c = {1: 2, 2: 2}
print("operator.eq(a,b): ", operator.eq(dict_a, dict_b))
print("operator.eq(c,b): ", operator.eq(dict_a, dict_c))
# 复杂的比较就懒得比较了
