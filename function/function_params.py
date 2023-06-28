#
# @author xiashuo
# @date 2023/6/4 23:42
#


def info(age, name):
    return print(f"我的名字是：{name},年龄是：{age}")


# 必需输入 name 和 age，否则报错
# TypeError: info() missing 2 required positional arguments: 'age' and 'name'
# info()
info(12, "xiashuo")
# 使用关键字参数允许函数调用时参数的顺序与声明时不一致，因为 Python 解释器能够用参数名匹配参数值。
info(name="xiashuo1212", age=20)


## 参数默认值
def test_default_params(name="xiashuo.xyz"):
    print(f"name: {name} ")


# 默认参数值
test_default_params()
# 指定的参数值
test_default_params('aaaa')


# 元组类型的参数
def add(*num0):
    sum = 0
    for i in num0:
        sum += i
    return sum


print(add(12, 13, 15))


# 将传入的多个参数以元组类型保存
def add(*num0):
    sum = 0
    for i in num0:
        sum += i
    return sum


print(add(12, 13, 15))


# 参数名以`*`开头的参数 前面的参数保证每一个都有值，剩下的都给以`*`开头的参数，同时后面的参数都必须以关键字参数的方式传
def test_astrisk_params(a, *b, c):
    print(a, b, c)


# a 为 a
# b 为内容为 ('b', 'c', 'd', 'e', 'f', 'f') 的元组
# c 为 &&  为关键字参数
print(test_astrisk_params(*"abcdef", c="&&"))


# 将传入的多个参数以字典类型保存
def add_new(**num1):
    sum = 0
    for i in num1.values():
        sum += i
    return sum


# key 不能是数字
print(add_new(e=12, f=13, g=15))


# 以`**`开头的参数都是参数列表的最后一个参数。
def test_double_astrisk_params(a, **b):
    print(a, b)


# key 不能是数字
test_double_astrisk_params(a=10, e=12, f=13, g=15)


def test_double_astrisk_and_astrisk_params(a, *b, c, **d):
    print(a, b, c, d)


# c 在 以`*`开头的参数的后面，因此，必须为关键字参数
# a 的值由字符串解包，为 "a"
test_double_astrisk_and_astrisk_params(*"abcde", c="fgh", f=13, g=15)
# a 的值由位置参数直接指定，为 10
test_double_astrisk_and_astrisk_params(10, *"abcde", c="fgh", f=13, g=15)

# 星号 * 后的参数必须用关键字的格式传入, * 前面的不做限制
def test_asterisk(name, age, *, hobby):
    return print(f"我的名字是：{name},年龄是：{age},爱好是{hobby}")


# TypeError: test_asterisk() takes 2 positional arguments but 3 were given
# test_asterisk("xiashuo", 45, "钓鱼")
test_asterisk("xiashuo", 45, hobby="钓鱼")
test_asterisk(age=60,name="xiashuo2", hobby="钓鱼")


def keywords(*, name, age):
    return print(f"我的名字是：{name},年龄是：{age}")


keywords(name="xiashuo", age=12)

# 则斜杠 / 前面的参数必须用位置参数的格式传入，`/`后面的不做要求
def positional_arguments(name, age, hobby, /, family):
    return print(f"我的名字是：{name},年龄是：{age},爱好是{hobby},我的家庭是{family}")


# TypeError: positional_arguments() got some positional-only arguments passed as keyword arguments: 'name, age'
# positional_arguments("钓鱼",age=12, name="xiashuo",family="虾家")
positional_arguments("xiashuo", 12, "钓鱼", family="虾家")
positional_arguments("xiashuo3", 35, "钓鱼", "虾家")

# `/` 和 `*` 混合使用，显然，`/` 必须在 `*` 的前面
def f(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)

f(10, 20, 30, d=40, e=50, f=60)
# f(10, b=20, c=30, d=40, e=50, f=60)   # b 不能使用关键字参数的形式
# f(10, 20, 30, 40, 50, f=60)           # e 必须使用关键字参数的形式
