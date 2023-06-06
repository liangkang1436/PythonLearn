#
# @author xiashuo
# @date 2023/6/6 7:41
#

num = 100

def test_1():
    # 在函数内部是可以直接使用全局变量的
    print(f"test_1：{num}")


def test_2():
    # 在函数内部是可以直接使用全局变量的
    print(f"test_2：{num}")


test_1()
test_2()
print(f"outer：{num}")
print("------------------------------------------------")


def test_3():
    # 下面的语句提示 Unresolved reference 'num' ，说明这个num无法指向全局的num
    # num += 50
    # 此时这个num不是全局的num，而是 test_3 这个方法内部的局部变量 num
    # 对这个局部变量的定义/修改不会影响到全局变量
    num = 200
    print(f"test_3：{num}")


test_1()
# test_3 中定义的是局部变量，不会影响外部的全局变量
test_3()
# 全局变量并没有变化
print(f"outer：{num}")
print("------------------------------------------------")


def test_4():
    # 声明 num 就是全局变量
    global num
    num = 200
    print(f"test_4：{num}")


test_1()
test_4()
# 全局变量同步了变化
print(f"outer：{num}")
print("------------------------------------------------")


# global 提供了一种，在函数内部，定义全局变量的方式，这样我们写代码的时候就更加灵活了
def test_5():
    # 声明 age 就是全局变量
    global age
    age = 600
    print(f"test_5：{age}")


def test_6():
    # 直接使用 age 这个全局变量
    print(f"test_6：{age}")


# 此时 test_5 必须在 test_6 的前面被调用
# 可能会有问题
test_5()
test_6()
print(f"outer：{age}")
