#
# @author xiashuo
# @date 2023/7/4 16:54
#

iter_01 = iter("abc")
print(next(iter_01))
print(next(iter_01))
print(next(iter_01))
# next方法获取最后一个元素之后再调用next，会报错 StopIteration
# StopIteration 异常用于标识迭代的完成，防止出现无限循环的情况
# print(next(iter_01))
# 你也可以给一个默认值来避免报错
print(next(iter_01, "我靠"))

iter_02 = iter("abcdef")
# while 循环 配合 迭代器的 next 方法
# 注意处理 StopIteration 异常
# 但是直接使用for循环不会报这个错
while True:
    try:
        print(next(iter_02), end=" | ")
    except StopIteration:
        print("迭代结束")
        break

# 迭代range对象
iter_03 = iter(range(0, 10))
for x in iter_03:
    print(x, end=" | ")

print()

# 迭代元组
tuple_01 = (*range(0, 10),)
iter_04 = iter(tuple_01)
for x in iter_04:
    print(x, end=" | ")

print()

# 迭代列表
iter_05 = iter([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
for x in iter_05:
    print(x, end=" | ")

print()


# 创建一个实现了迭代器的类

class MyIterator:
    def __iter__(self):
        self.a = 1
        return self

    # def __next__(self):
    #     """注意，这种实现是可以无限得带下去的"""
    #     x = self.a
    #     self.a += 1
    #     return x

    def __next__(self):
        if self.a <= 10:
            x = self.a
            self.a += 1
            return x
        else:
            # StopIteration 异常用于标识迭代的完成，防止出现无限循环的情况，在 __next__() 方法中我们可以设置在完成指定循环次数后触发 StopIteration 异常来结束迭代。
            raise StopIteration


myIterator = MyIterator()
myiterObj = iter(myIterator)
for x in myiterObj:
    print(x, end=" | ")

print()


# 包含yield关键字的函数，是一个生成器函数，一个生成器函数对象，概念上就是一个迭代器，跟迭代器的用法一样

def countdown(n):
    while n > 0:
        yield n
        n -= 1


# 创建生成器对象
# 一个生成器对象,也是一个迭代器对象
generator = countdown(5)
# 输出 <class 'generator'>
# 如果不包含yield 关键字,类型为 function
print(type(generator))

# 通过迭代生成器获取值
print(next(generator))  # 输出: 5
print(next(generator))  # 输出: 4
print(next(generator))  # 输出: 3

# 使用 for 循环迭代生成器
for value in generator:
    print(value)  # 输出: 2 1


# 在一个 generator function 中，如果没有 return，则默认执行至函数完毕，如果在执行过程中 return，则直接抛出 StopIteration 终止迭代。
# 带有return的生成器
def countdown_with_return(n):
    while n > 0:
        yield n
        n -= 1
        if n == 2:
            # 使用该return则排出错误
            # 抛出错误 StopIteration
            return


generator_with_return = countdown_with_return(3)
# 输出3
print(next(generator_with_return))
# 报错，输出 StopIteration
# print(next(generator_with_return))

# 判断是不是生成器

from inspect import isgeneratorfunction


def test_function():
    print("test")


# True
print(isgeneratorfunction(countdown))
# False
print(isgeneratorfunction(test_function))
# False
print(isgeneratorfunction(lambda: print()))


# 简单实践,输出斐波那契数列
# 生成器本质上是一个产生迭代器的函数,作用类似于前面的自定义迭代器类
def fibonacci(n):
    count, a, b = 1, 1, 2
    while count <= n:
        yield a
        a, b = b, a + b
        count += 1


fibonacci_generator = fibonacci(5)
for i in iter(fibonacci_generator):
    print(i, end=" | ")

print()
