#
# @author xiashuo
# @date 2023/6/5 13:57
#

def add_num(*nums):
    sum = 0
    for i in nums:
        sum += i

    return sum


sum = add_num(12, 12, 45)
print(sum)


def test_none():
    pass

# var 的值是 None ，类型是 NoneType
var = test_none()
print(var,type(var))

def test_none2():
    # 也可以直接返回None
    return None