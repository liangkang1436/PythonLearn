#
# @author xiashuo
# @date 2023/7/9 16:56
#
import os
import sys

a = 10
# if a < 10:
#     print(a)

# print(f"{a+'aaa'}")

print("---- try/except ----")

# try/except
try:
    print(f"{12 / 0}")
    print("it's ok")
# 一个 try 语句可能包含多个 except 子句，分别来处理不同的特定的异常。最多只有一个分支会被执行
except ValueError as error:
    print(f"输出 {error}")
    # 使用 raise 语句直接将捕获的异常抛出，甚至都不需要异常的变量名
    raise
except ZeroDivisionError as error:
    print("error occurred")
    print(f"输出 {error}")
# 你可以把多个异常写到一起，放到一个元组里
except (RuntimeError, TypeError, NameError) as error:
    print(f"输出 {error}")
# 可以捕获所有的异常，这个一般放在最后，这样可以用于捕获任意异常
except Exception as e:
    print(e)
# 上面的 except 也可以省略异常的类型
except:
    print("uncaught exception,just raise it")
    # 使用 raise 语句直接将捕获的异常抛出，甚至都不需要异常的变量名
    raise

print("---- over ----")

print("---- else ----")

# else 子句
try:
    print(f"{12 / 2}")
    print("it's ok")
except ZeroDivisionError as error:
    print("error occurred")
    print(f"输出 {error}")
except:
    print("uncaught exception,just raise it")
    # 使用 raise 语句直接将捕获的异常抛出，甚至都不需要异常的变量名
    raise
else:
    print("it's alright")

print("---- over ----")
print("---- finally ----")

# finally 子句
try:
    print(f"{12 / 0}")
    print("it's ok")
except ZeroDivisionError as error:
    print("error occurred")
    print(f"输出 {error}")
except:
    print("uncaught exception,just raise it")
    # 使用 raise 语句直接将捕获的异常抛出，甚至都不需要异常的变量名
    raise
else:
    print("it's alright")
finally:
    print("finally action : calculate over ")

print("---- over ----")

# 如果 try 中的错误没有被 except 子句拦截，则 finally 之后 抛出错误
try:
    # print(f"{12 / 0}")
    print("it's ok")
finally:
    print("finally action : calculate over ")

print("---- over ----")
# 输出错误

print("---- except return ----")


# 通过注释 try-except-else-finally 中各个子句的 return 语句来看看最终生效的是哪个 return
def try_return():
    print("try_return")
    return 11


def test_return_in_excetp():
    try:
        print(f"{12 / 0}")
        print("it's ok")
        # return try_return()
    except ZeroDivisionError as error:
        print("error occurred")
        print(f"输出 {error}")
        return 12
    except:
        print("uncaught exception,just raise it")
        # 使用 raise 语句直接将捕获的异常抛出，甚至都不需要异常的变量名
        raise
    else:
        print("it's alright")
        return 13
    finally:
        print("finally action : calculate over ")
        return 14

    print("function run")
    return 20


print(test_return_in_excetp())

print("---- finally 不会修改 return 语句的值 ----")

value = 10

def try_return():
    print("try_return")
    return value


def test_return_in_excetp():
    try:
        # print(f"{12 / 0}")
        print("it's ok")
        return try_return()
    except ZeroDivisionError as error:
        print("error occurred")
        print(f"输出 {error}")
        return 12
    except:
        print("uncaught exception,just raise it")
        # 使用 raise 语句直接将捕获的异常抛出，甚至都不需要异常的变量名
        raise
    else:
        print("it's alright")
        return 13
    finally:
        print("finally action : calculate over ")
        value = 11

        # return 14

    print("function run")
    return 20


print(test_return_in_excetp())


print("---- over ----")

# 输出错误信息到文件中
import traceback

try:
    print(f"{12 / 0}")
except ZeroDivisionError as error:
    print("error occurred")
    # print_exc 不指定输出文件对象的话，默认输出到 sys.stderr 文件对象
    traceback.print_exc(file=open("./error.txt", "a"))

print("---- with ----")


class test_keyword_with():

    def do_work(self):
        print("doing work")
        print(12 / 0)

    def __enter__(self):
        print("enter obj")
        # 重点，需要返回当前对象，这个对象将赋值给 with as 语句中 as 后面的那个变量
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit obj")
        # 通过 exc_type（异常类型）, （exc_val）异常信息 我们可以处理异常信息；exc_tb 异常栈对象
        # 类型比较，直接比较即可
        if exc_type is not None:
            # 可以针对特定类型进行处理，比如日志输出
            # 注意，我们没有办法在这里取消异常的抛出，也就是人们常说的吃掉这个异常
            print(exc_val)


# with test_keyword_with() as with_obj:
#     with_obj.do_work()

# as 也可以省略，此时 __enter__ 方法可以不返回对象
with_obj = test_keyword_with()
with with_obj:
    # 在这里进行了处理，__exit__ 方法中就不会有异常信息了
    try:
        with_obj.do_work()
    except ZeroDivisionError as e:
        print("exception occur",e)

print("---- over ----")

# @contextmanager 装饰器

from contextlib import contextmanager  # 导入上下文管理器


# @contextmanager
@contextmanager
def get_file_obj():
    # 创建一个空文件
    empty_file_name = "./emptyfile.txt"
    empty_file_obj = open(empty_file_name, "w")
    empty_file_obj.close()
    empty_file_obj = open(empty_file_name, "r")

    file_obj = None
    try:
        # 文件不存在
        file_obj = open("./test.txt", "r", encoding="utf-8")
        yield file_obj
    except Exception as error:
        # 可以捕捉到异常并阻止异常的抛出，但是此时我们仍然需要返回空的文件对象给 with as 语句
        print("文件不存在")
        yield empty_file_obj
    finally:
        empty_file_obj.close()
        # 删除临时文件
        os.remove(empty_file_name)
        if file_obj != None:
            file_obj.close()


with get_file_obj() as file_obj:
    print(file_obj.readlines())

print("---- raise ----")

# 手动抛出异常
b = 10
if b == 10:
    # 手动抛出 ArithmeticError 异常，自定义异常提示信息
    # raise ArithmeticError(f"b 的值不对：{b}")
    # 或者直接抛出类
    # raise ZeroDivisionError
    pass

print("---- customize except ----")


# 自定义异常
class MyError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

# raise MyError("自定义错误类型")
