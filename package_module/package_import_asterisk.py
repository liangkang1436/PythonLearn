#
# @author xiashuo
# @date 2023/7/25 8:05
#

# import aaa.bbb.ccc
# print(aaa.bbb.ccc.name)

# from aaa.bbb import ccc
#
# # 增加符号 ccc
# print(dir())
# # 可直接通过ccc来调用
# print(ccc.name)

# from aaa import bbb
# # module 'aaa.bbb' has no attribute 'ccc'
# # 从这个报错信息中也可以看出， 包'aaa.bbb' 确实是被识别为了一个模块
# print(bbb.ccc.name)

# ----------------------------------------------------------------

# from aaa.bbb.ccc import *
# # 把 aaa.bbb.ccc 当成一个模块来理解
# print(name)


# 导入了 bbb 这个子包，并将其当作一个模块来看待
# from aaa import *

# 导入了 ccc 这个子包，并将其当作一个模块来看待
# from aaa.bbb import *
# print(ccc.name)

# from aaa.bbb.ccc import *
# print(xiashuo.name)
# print(xiashuo.age)
# xiashuo.info()
