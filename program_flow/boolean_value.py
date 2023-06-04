#
# @author xiashuo
# @date 2023/6/4 11:59
#


true_value = True
print(true_value, type(true_value))
false_value = False
print(false_value, type(false_value))
greater = 10 > 5
print(f"{greater}, {type(greater)}")
# == 等效于 equal = "12133".__eq__("12133")
equal = "12133" == "12133"
print(equal)
print("--------------")
equal = 12133 == "12133"
print(equal)
print("--------------")
print(f"{1200000 == 1200000}")
print("--------------")
# 类型转换函数 bool() ，只要参数不是数字0，就返回True，否则返回False
print(bool(1))
print(bool(10))
print(bool(0))
print(bool(-120))
print(bool("0"))
print(bool("-120"))
print("--------------")
# 逻辑运算符
print(not (1 != 1))
print((1 != 1) or (1 != 2))
print((1 == 1) and (2 == 2))
