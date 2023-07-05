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

print("--------------")

# 当一个值被用作条件表达式时，它会被隐式地转换为布尔类型，可能是通过bool()函数来确定其是True 还是 False
# 空字符串、空列表、空元组、空字典、数字 0 、None 等对象的布尔值为 False
# False
print(bool(""))
# False
print(bool(list()))
# False
print(bool(tuple()))
# False
print(bool(set()))
# False
print(bool(dict()))
# False
print(bool(0))
# False
print(bool(None))
# 使用 not 将其变成 True
# True
print(bool(not ""))

if list():
    print("True")
else:
    print("False")

# 类型不同，通过`==`比较，一定是`False`，反之通过`!=`比较，一定是`True`。
if '' != True:
    print("'' 不为 True")

if '' != False:
    print("'' 不为 False")

# 会自动调用bool()函数判断其是 True 还是 False
# bool('') False
if '':
    print("'' 逻辑上为 True")
else:
    print("'' 逻辑上为 False")

# bool( not '') True
if not '':
    print(" not '' 为true ")
