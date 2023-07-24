#
# @author xiashuo
# @date 2023/7/19 13:54
#
import builtins
import sys

# 不知道为什么，Python给我一种感觉，就是Python比Java更接近系统底层，不知道是不是因为Python比Java离C更近

print("---------------------------------"+"sys.argv"+"---------------------------------")
for arg in sys.argv:
    print(arg)
print("---------------------------------"+"sys.path"+"---------------------------------")
for path in sys.path:
    print(path)

print("---------------------------------"+"sys.modules"+"---------------------------------")
for name,module in sys.modules.items():
    print(name,"-",module)

# 重定向 stdout
# sys.stdout = open("./sys_out.txt","w",encoding="utf-8")
# 从这里开始，往后的所有输出都会输出到 sys_out.txt 文件中，而不是控制台中
# print("输出")

print("---------------------------------"+"sys.builtin_module_names"+"---------------------------------")
for module_name in sys.builtin_module_names:
    print(module_name)
print("---------------------------------"+"sys.copyright"+"---------------------------------")
print(sys.copyright)
print("---------------------------------"+"sys.exec_prefix"+"---------------------------------")
print(sys.exec_prefix)
print("---------------------------------"+"sys.prefix"+"---------------------------------")
print(sys.prefix)
print("---------------------------------"+"sys.executable"+"---------------------------------")
print(sys.executable)
print("---------------------------------"+"sys.float_info"+"---------------------------------")
print(sys.float_info)
print("---------------------------------"+"sys.float_repr_style"+"---------------------------------")
print(sys.float_repr_style)
print("---------------------------------"+"sys.hexversion"+"---------------------------------")
print(sys.hexversion)
print("---------------------------------"+"sys.implementation"+"---------------------------------")
print(sys.implementation)
print("---------------------------------"+"sys.maxsize"+"---------------------------------")
print(sys.maxsize)
print("---------------------------------"+"sys.maxunicode"+"---------------------------------")
print(sys.maxunicode)
print("---------------------------------"+"sys.platform"+"---------------------------------")
print(sys.platform)
print("---------------------------------"+"sys.thread_info"+"---------------------------------")
print(sys.thread_info)
print("---------------------------------"+"sys.version"+"---------------------------------")
print(sys.version)
print("---------------------------------"+"sys.version_info"+"---------------------------------")
print(sys.version_info)
print("---------------------------------"+"sys.dllhandle"+"---------------------------------")
print(sys.dllhandle)
print("---------------------------------"+"sys.winver"+"---------------------------------")
print(sys.winver)
print("---------------------------------"+"sys.displayhook()"+"---------------------------------")
aa = "xiashuo.xyz"
sys.displayhook(12)
sys.displayhook(aa)
print(builtins._)
print("---------------------------------"+"sys.getprofile()"+"---------------------------------")
sys.getprofile()
print("---------------------------------"+"sys.getrefcount()"+"---------------------------------")
# 使用 sys.getrefcount() 方法来查看整数和字符串的引用次数结果会比较难以判定，因为Python对其有内存优化
print(sys.getrefcount(aa))
# 返回 3
print(sys.getrefcount(121545))
class Ref_test():
    pass
# 正常，只会返回 1，也就是除了sys.getrefcount引用之外没有人引用
print(sys.getrefcount(Ref_test()))
print("---------------------------------"+"sys.getsizeof()"+"---------------------------------")
# 对象不包含任何内容，但是依然占据了内存
print(sys.getsizeof(Ref_test()))
print("---------------------------------"+"sys.getrecursionlimit()"+"---------------------------------")
print(sys.getrecursionlimit())

print("---------------------------------dynamic sys.path---------------------------------")
# 动态添加  C:/Users/wwwli/Desktop/script 到 path
sys.path.append("C:/Users/wwwli/Desktop/script")
from aaa import abcd
from aaa import ABCD
print(abcd)
print(ABCD())
