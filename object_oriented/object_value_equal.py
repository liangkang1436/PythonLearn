#
# @author xiashuo
# @date 2023/7/17 7:30
#

# is 和 ==
# ==比较的是两个对象的内容是否相等，即内存地址可以不一样，内容一样就可以了；而is比较的是两个实例对象内存地址是否一样。
# 我们可以通过重写类的 __eq__ 来自定义通过 == 时的行为，这叫运算符重载，内置类型均已重载 __eq__ 所以可以实现 根据对象内容比较，自定义类需要自行重写 __eq__ 来实现通过 == 比较时根据内容判断是否相等
# 在 Java 中  ==  用于比较对象内存，而equals方法比较对象内容，只不过Java无法实现运算符重载，不能自定 == 行为，不然也不需要equals方法了

print("-----------数字----------------")
# 数字
a = 1245678985
b = int(1245678985)
# True
print(a is b)
# True
print(a == b)

print("-----------小数----------------")
# 小数
a = 12456.78985
b = float(12456.78985)
# True
print(a is b)
# True
print(a == b)

print("-----------字符串----------------")
# 字符串
a = "1245678985"
b = str("1245678985")
# True
print(a is b)
# True
print(a == b)

print("-----------长字符串----------------")
# 长字符串
a = "hello world hello world hello world hello world hello world hello world hello world hello world hello world hello world "
b = "hello world hello world hello world hello world hello world hello world hello world hello world hello world hello world "
# True
print(a is b)
# True
print(a == b)

print("-----------bool----------------")
# bool
# True
print(True is True)
# True
print(True == True)

print("-----------列表----------------")
# 列表
a = ["12", 45, True]
b = ["12", 45, True]
# False
print(a is b)
# True
print(a == b)

print("-----------集合----------------")
# 集合
a = {12, 78, "aaa"}
b = {"aaa", 78, 12}
# False
print(a is b)
# True
print(a == b)

print("-----------None----------------")
# None
# False
print(None is not None)
# True
print(None is None)


print("-----------自定义类----------------")
class test_value_equal:
    def __init__(self, name: str, age: int):
        self.name: str = name
        self.age: int = age

    # 如果不重写 __eq__， a == b 会返回false
    def __eq__(self, other):
        return self.name == other.name and self.age == other.age


a = test_value_equal("xiashuo.xyz", 12)
b = test_value_equal("xiashuo.xyz", 12)
# False
print(a is b)
# 需要重写 __eq__ 方法，否则返回false。
# True
print(a == b)

print("-----------跨方法----------------")
# 跨调用栈
a = "xiashuo.xyz"

def test_value():
    b = "xiashuo.xyz"
    # True
    print(a is b)
    # True
    print(a == b)

test_value()

print("-----------跨类----------------")
# 跨类
class test_obj:
    def __init__(self):
        self.name = "xiashuo.xyz"

obj = test_obj()
# True
print(a is obj.name)
# True
print(a == obj.name)


print("-----------跨模块----------------")

from test_value import c

a = "xiashuo.xyz"
# False
print(a is c)
# True
print(a == c)