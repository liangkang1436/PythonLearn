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

# 如果参数名以`*`开头的参数后面还有参数，则后面的参数都必须以关键字参数的方式传入
def test_astrisk_params(a, *b, c):
    print(a, b, c)

# a 为 a
# b 为内容为 ('b', 'c', 'd', 'e', 'f', 'f') 的元组
# c 为 &&  为关键字参数
print(test_astrisk_params(*"abcdef",c="&&"))


# 将传入的多个参数以字典类型保存
def add_new(**num1):
    sum = 0
    for i in num1.values():
        sum += i
    return sum


# key 不能是数字
print(add_new(e=12, f=13, g=15))


def test_asterisk(name, age, *, hobby):
    return print(f"我的名字是：{name},年龄是：{age},爱好是{hobby}")


# TypeError: test_asterisk() takes 2 positional arguments but 3 were given
# test_asterisk("xiashuo", 45, "钓鱼")
test_asterisk("xiashuo", 45, hobby="钓鱼")


def keywords(*, name, age):
    return print(f"我的名字是：{name},年龄是：{age}")


keywords(name="xiashuo", age=12)


def positional_arguments(name, age, hobby, /, family):
    return print(f"我的名字是：{name},年龄是：{age},爱好是{hobby},我的家庭是{family}")


# TypeError: positional_arguments() got some positional-only arguments passed as keyword arguments: 'name, age'
# positional_arguments("钓鱼",age=12, name="xiashuo",family="虾家")
positional_arguments("xiashuo", 12, "钓鱼", family="虾家")

# def f(a, b, /, c, d, *, e, f):
#     print(a, b, c, d, e, f)
#
# f(10, 20, 30, d=40, e=50, f=60)
# f(10, b=20, c=30, d=40, e=50, f=60)   # b 不能使用关键字参数的形式
# f(10, 20, 30, 40, 50, f=60)           # e 必须使用关键字参数的形式
