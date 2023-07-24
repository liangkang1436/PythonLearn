#
# @author xiashuo
# @date 2023/7/24 17:00
#

import test_target

print(test_target.aaa)
test_target.test_info()
test_obj = test_target.Test_Import()

from test_target import aaa,test_info,Test_Import
print(aaa)
test_info()
test_obj_2 = Test_Import()

# 可以直接用 * 表示模块内所有的变量方法和类，但是一般不建议这么写
# 如果使用通配符从模块中导入所有名称，则Python不会导入带有单个前置下划线的名称（除非模块定义了覆盖此行为的__all__列表）
# 应该避免通配符导入，因为它们使名称空间中存在哪些名称不清楚。 为了清楚起见，坚持常规导入更好。
from test_target import *

print(_bb)
print(aaa)
test_info()
test_obj_2 = Test_Import()