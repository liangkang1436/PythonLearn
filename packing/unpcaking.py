#
# @author xiashuo
# @date 2023/6/25 17:44
#

print("------------------------------ 变量赋值过程中的自动解包 ------------------------------")

print("--------------- 容器的自动解包 ---------------")
# 两个变量的类型都是 str
char_a, char_b = "ab"
print(char_a, type(char_a), char_b, type(char_b))
# 两个变量是int类型
list_ele_a, list_ele_b = [1212, 1313]
print(list_ele_a, type(list_ele_a), list_ele_b, type(list_ele_b))
# 两个变量是字符串类型
tuple_ele_a, tuple_ele_b = ("bbbb", "cccc")
print(tuple_ele_a, type(tuple_ele_a), tuple_ele_b, type(tuple_ele_b))
# 元组的隐式声明
tuple_ele_a, tuple_ele_b = "bbbb", "cccc"
print(tuple_ele_a, type(tuple_ele_a), tuple_ele_b, type(tuple_ele_b))
# 变量都是int类型，且元素并不是按照 1414, 1515, 1616, 1717赋值，而是任意顺序
set_ele_a, set_ele_b, set_ele_c, set_ele_d = {1414, 1515, 1616, 1717}
print(set_ele_a, type(set_ele_a), set_ele_b, type(set_ele_b), set_ele_c, type(set_ele_c), set_ele_d, type(set_ele_d))
# 字典的自动解包，只获取了key，丢掉了val
# 变量都是int类型，且元素按照 1414, 1515, 1616, 1717赋值
dict_ele_a, dict_ele_b, dict_ele_c, dict_ele_d = {1818: "aa", 1919: "bb", 2020: "cc", 2121: "dd"}
print(dict_ele_a, type(dict_ele_a), dict_ele_b, type(dict_ele_b), dict_ele_c, type(dict_ele_c), dict_ele_d,
      type(dict_ele_d))

# 如果可迭代对象中元素的个数大于接收变量的个数怎么办？ 在其中一个变量名前加上 *，注意只能给一个变量加，给两个加会报错
# 最终的效果就是带 * 号的变量变成一个列表，且带 * 号的变量包含的元素中的值在等号右侧的相对位置，跟变量在等号左侧的变量列表所处的相对位置相同
a, *b, c = [1, 2, 3, 4, 5]
# 1 [2, 3, 4] 5
print(a, b, c)
a, *b, c = (1, 2, 3, 4, 5)
# b依然是一个列表
# 1 [2, 3, 4] 5
print(a, b, c)
a, *b, c = {1, 2, 3, 4, 5}
# b依然是一个列表
# 1 [2, 3, 4] 5
print(a, b, c)

# 如果可迭代对象只包含一个元素，我只想要这个元素，而不是想要这个可迭代对象对象，在变量后面加一个逗号即可
# a 为 int 类型
a, = [1]
print(a, type(a))
# a 为 list 类型
a = [1]
print(a, type(a))

print("--------------- 多变量的赋值 ---------------")
# 多变量的赋值与交换本质上也是自动解包，因为等号右边的会被看作是元组对象
int_a, int_b, int_c = 1, 2, 3
print(int_a, type(int_a), int_b, type(int_b), int_c, type(int_c))
# 实际上等价于
int_a, int_b, int_c = (1, 2, 3)
print(int_a, type(int_a), int_b, type(int_b), int_c, type(int_c))

print("--------------- 多变量的交换 ---------------")
# 不需要声明第三个变量的两值交换，牛逼
int_a, int_b, int_c = int_c, int_a, int_b,
# 3 1 2
print(int_a, int_b, int_c)
int_a, int_b, int_c = int_c - int_a, int_c + int_b, int_a + int_b,
# -1 3 4
print(int_a, int_b, int_c)

# 计算斐波那契数列
a = 0
b = 1
for i in range(10):
    a, b = b, a + b
# 输出 89
print(b)

print("------------------------------ 表达式中的解包 ------------------------------")
# 我们在学习各种容器的各种API，本质上是把容器当成一个整体来操作，这种操作是无法跨容器类型的，现在有了解包操作，我们可以直接对容器中的元素进行操作，自然也就不存在容器类型的限制了

tuple_1 = *range(4), 4
# (0, 1, 2, 3, 4)
print(tuple_1)
# [0, 1, 2, 3, 4]
print([*range(4), 4])
# {0, 1, 2, 3, 4}
print({*range(4), 4})
# 这个操作实际上相当于拼接了两个字典
# **对字典的解包，只能用在{}内部，好像是这样
# {'x': 1, 'y': 2, 'z': 3}
print({'x': 1, **{'y': 2, 'z': 3}})
# 例如，相当于啥都没做
dict_ele_a, dict_ele_b = {**{"a": 1, "b": 3}}
print(dict_ele_a, dict_ele_b)

# list的拼接
list_raw = ["a", "b", "c"]
list_compose = [*range(4), *list_raw]
# 输出 [0, 1, 2, 3, 'a', 'b', 'c']
print(list_compose)

tuple_raw = ("1", "2", "3")
tuple_compose = (*tuple_raw, *range(4))
# 输出 ('1', '2', '3', 0, 1, 2, 3)
print(tuple_compose)

set_raw = {"1", "2", "3"}
set_compose = {*set_raw, *range(4)}
# 输出 {0, 1, 2, 3, '1', '3', '2'}
print(set_compose)

# 两个字典的拼接
dict_raw = {'x': 1, 'y': 2, 'z': 3}
dict_compose = {"a": "bc", **dict_raw}
# 输出 {'a': 'bc', 'x': 1, 'y': 2, 'z': 3}
print(dict_compose)

# 以上好像看不出什么，现在才是解包的妙用
# 将元组和集合中的元素合并成一个列表
tuple_2_use = ("1", "2", "3",)
set_2_use = {"a", "b", "c"}
list_result = [*tuple_2_use, *set_2_use]
# 输出 ['1', '2', '3', 'c', 'a', 'b']
print(list_result)

print("------------------------------ 函数调用过程中的解包 ------------------------------")


# 需要用到 * 和 **
def func_test_unpacking(a, b, c):
    print(a, b, c)


def func_test_unpacking_over(a, *b, c):
    print(a, b, c)


func_test_unpacking(*"abc")
func_test_unpacking(*["aaa", "bbb", "ccc"])
func_test_unpacking(*(1, 1, 1))
func_test_unpacking(*{1, "aa", "bbb"})
# 如果传入的参数多了，函数也可以用 * 参考  《函数.md》中的 参数名以*开头 小节
# 输出 a ('b', 'c', 'd', 'e', 'f', 'g') &&
# a 为 a
# b 为内容为 ('b', 'c', 'd', 'e', 'f', 'g') 的元组
# c 为 &&  为关键字参数
func_test_unpacking_over(*"abcdefg", c="&&")

# 字典有点特殊
# 用 * 来解包字典的时候，会跟前面一样将key作为结果传入函数
# 输出 1 2 3
func_test_unpacking(*{1: "c", "2": "b", 3: "c"})
# 用 ** 来解包字典的时候，会以关键字参数的形式传入参数，其中字典的key就是对应参数名，val就是参数值
# 注意字典不能包含比方法参数多的key，不然会报错，能不能少得看少的那个关键字参数有没有默认值，有的话就可以省略
# 输出 10 11 12
func_test_unpacking(**{"a": 10, "b": 11, "c": 12})
