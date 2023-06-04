#
# @author xiashuo
# @date 2023/6/3 9:52
#


num = 10 + 20
divide = 11
a = num / divide
print(a)
# 整形取整
a = num // divide
print(a)
# 就算是float，用 // 也能得到一个整数结果
a = 20.12 // divide
print(a)
a = num % divide
print(a)
# 指数运算符，在Java中是没有了，Java只能通过函数实现指数运算
a = 10 ** 3
print(a)


# 赋值运算符
c = 100
c += 5
print(c)
c -= 10
print(c)
c /= 2
print(c)
c //= 3
print(c)
c %= 10
print(c)
c **= 2
print(c)

# 运算符的优先级
# 先计算指数，再乘以10
num = 10*12**3
print(num)

