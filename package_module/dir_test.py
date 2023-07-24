#
# @author xiashuo
# @date 2023/7/24 20:13
#
import test_target

# 模块对象
print(dir(test_target))


class dir_test():
    def __init__(self):
        self.name = 'test'
        self.age = 12

    def __dir__(self):
        return ['222']


class_ojb = dir_test()
print(dir(class_ojb))

# 数字对象
print(dir(12))

# 字符串对象
print(dir("xiashuo.xyz"))
