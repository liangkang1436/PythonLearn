#
# @author xiashuo
# @date 2023/6/6 7:28
#




# 调用函数的语句需要在定义函数的语句之后
# 但是函数在嵌套调用的时候，不需要保证被调用的方法在调用别的方法之前定义
def test_1(name,age):
    print(f"{name},{age}")
    sum_val = sum(2, 6)
    print(f"sum:{sum_val}")

def sum(a,b):
    return a+b

test_1(age=12,name="xiashuo")