#
# @author xiashuo
# @date 2023/7/24 16:59
#

aaa = "xiashuo"

_bb = "baidu.com"


def test_info():
    print("Hello, bro shu")


class Test_Import():
    pass


__all__ = ["aaa", "_bb", "test_info", "Test_Import"]

def __dir__():
    return ["111"]

run_flag = 0

if __name__ == "__main__":
    run_flag = 1
    print("i am running by myself")
else:
    run_flag = 2
    print("i am imported")



