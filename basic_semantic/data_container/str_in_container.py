#
# @author xiashuo
# @date 2023/6/12 10:54
#

# 从容器视角看字符串
print("------------------------------初始化----------------------------------")
# 直接通过方法创建一个
str_empty = str()
print(str_empty, type(str_empty))

str_now = "abcdefg123456"

print("------------------------------读取字符串中的子字符/子字符串----------------------------------")

# 通过索引访问字符，第一个字符下表为0
print(str_now[0])
print(str_now[2])
# 从后向前访问字符，最后一个字符为-1
print(str_now[-1])
print(str_now[-2])

# 截取字符串中的字符返回一个新的str
# 包含左边界，不包含右边界
print(str_now[1:2])
print(str_now[1:-2])
# 指定步长为2
# 结果的索引从0开始，然后是2，然后是4，以此类推
print("步长为2", str_now[::2])
# 左右边界可以不写，
# 左边界不写默认从第一个字符开始
print(str_now[1:])
# 右边界不写默认到最后一个字符
print(str_now[:-2])
# 左右都不写，那就是整个字符串
print(str_now[:])
# 当步长大于0的时候左边界必须小于右边界，否则输出空字符串
# 输出不为空
print(str_now[-2:-1])
# 输出为空
print(str_now[-1:-2])
# 当步长小于0的时候左边界必须大于右边界，否则输出空字符串
# 输出不为空
print(str_now[3:1:-1])
# 输出为空
print(str_now[1:3:-1])

sub_str = str_now[0:3]
# 无法直接更新指定索引的字符
# 'str' object does not support item assignment
# sub_str[1] = "$"

# 字符串的倒序操作
print(str_now)
print(str_now[::-1])

# 切片操作是可以连写的，灵活使用的话会非常方便
print(str_now[:6][::-1][2:])

print("------------------------------字符串元素的增删改查----------------------------------")

str_2_del = "i am dying"
print(str_2_del)
# 可以通过del删除字符串
del str_2_del
# print(str_2_del)

# 具体请看 str_function.py 中的实践
# 查询指定字符串在特定范围内第一次出现的位置
print(str_now.index("abc"))
# 在指定的范围内查找特定字符串出现的次数
print(str_now.count("123"))

print("------------------------------对字符串的整体操作----------------------------------")
# 字符串长度
print(len(str_now))

str_compare = "我的123456789abcdefg"
# 这里比较的好像是unicode的码点
print(max(str_compare))
# 字符串中的最大值
print(min(str_compare))

print("------------------------------对字符串的符号操作，非常方便----------------------------------")
str_new = "aaa-bbb-ccc-ddd"
str_2_plus = "1111-222-333-444-555"
# 可以直接通过 + 将两个字符串合并
plus = str_new + str_2_plus
print(plus)
# 原字符串不会受影响
print(str_new)

# 通过 *n 将字符串复制n倍
multiple = str_new * 4
print(multiple)
# 原字符串不会受影响
print(str_new)

# 直接通过 in 语句判断元素是否在字符串中，类似于 index 方法
print("-" in str_new)
print("aaa" in str_new)
# not in 判断元素是否不在字符串中
print("aaa" not in str_new)

# for-in 循环遍历tuple
for i in str_new:
    print(i, end=' ')
print()
print(str_new)

print("------------------------------字符串的比较----------------------------------")

# 导入 operator 模块
import operator

a = "12"
b = "23"
c = "23"
print("operator.eq(a,b): ", operator.eq(a, b))
print("operator.eq(c,b): ", operator.eq(c, b))

# 复杂字符串
str_str_0 = 'aaa-bb-cccccc-dd'
str_str_0_copy = 'aaa-bb-cccccc-dd'
str_str_1 = 'aaa-cccccc-dd-bb'
print(operator.eq(str_str_0, str_str_0_copy))
print(operator.eq(str_str_0, str_str_1))

print("------------------------------将别的容器对象转化为字符串----------------------------------")
# 从列表转化而来
str_from_list = str([12, 23.45])
# 输出  "[12, 23.45]"
print(str_from_list)
# 从元组转化而来
str_from_tuple = str((12, 23.45))
# 输出 "(12, 23.45)"
print(str_from_tuple)
# 从集合转化而来
str_from_set = str({12, 23.45})
# 输出 "{12, 23.45}"
print(str_from_set)
# 从字典转化而来
str_from_dict = str({"name": "12", "age": "23.45"})
# 输出 "{'name': '12', 'age': '23.45'}"
print(str_from_dict)
