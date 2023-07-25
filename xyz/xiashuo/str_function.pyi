#
# @author xiashuo
# @date 2023/7/10 11:27
#

def str_greeting() -> None: ...

# 在pyi中定义方法的类型信息跟直接在py中定义方法的类型信息在语法上的唯一的区别就是在pyi中方法体部分用 ... 代替
# 在这里声明方法和参数类型之后，使用这个方法的时候，就会有型提示
def show_info(name: str, age: int) -> None: ...
