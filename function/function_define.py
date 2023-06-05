#
# @author xiashuo
# @date 2023/6/4 23:18
#

# 可以直接在参数上设置默认值
def main(name="xiashuo.xyz"):
    print(f"{name} main function")
    return name + "-----"

# 因为python代码都是顺序执行的，我们调用函数之前，必须要保证这个函数已经定义了才可以，所以，对main函数的定义必须在对main函数的调用之前，否则会报错

# 使用参数的默认值
main()
main("aaa")
print(main("bbb"))

# 方法注释
def test_doc(aaa,bbb):
    """
    测试输出
    :param aaa:
    :param bbb:
    :return:
    """
    print(f"{aaa},{bbb}")
    return aaa


test_doc(12, "sdsd")










