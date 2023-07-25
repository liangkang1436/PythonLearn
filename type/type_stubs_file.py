#
# @author xiashuo
# @date 2023/7/9 20:41
#
# import xyz.xiashuo.str_function
from xyz.xiashuo.str_function import *

# tubs中没有声明这个方法，在这里，解释器会报错，但是依然可以成功运行
print(name)
print(age)

str_greeting()

show_info("sdf", 12)
# 虽然类型跟stubs中的类型不匹配，但仅仅是警告，没有报错
show_info("dfdfa", "dfsd")


