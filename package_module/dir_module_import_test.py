#
# @author xiashuo
# @date 2023/7/24 19:41
#

# 冲突变量
aaa = "aliyun"
test_info = "tencent"

print(dir())

print(aaa)
print(test_info)

from test_target import *
# 重命名的写法
# from test_target import aaa as aaa1,test_info as test_info2

print(dir())
# 第一种覆盖
# xiashuo
print(aaa)
# 第二种覆盖
# <function test_info at 0x00000211B7E6A320>
print(test_info)
