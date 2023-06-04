#
# @author xiashuo
# @date 2023/6/2 13:33
#

# 声明变量不需要指定类型
# 一行语句结束了也不需要用;来结尾，这个跟JavaScript一样
wallet = 45
# print可以直接指定多个参数，在输出结果中，多个参数用空格隔开
# 45 我靠 会自动拼接的吗
print("钱包里还剩下：", wallet, '这么多钱', '我靠', '会自动拼接的吗')
# 也可以通过 + 直接拼接字符串，但是要求+两端的内容的类型必须是字符串，
# 与Java不同，python没有自动类型转换
# 所以下面这种写法是错的，因为wallet是int类型
# print("钱包里还剩下："+wallet+"这么多钱")
# 但是如果 wallet 是一个字符串，那就可以，可以通过str()来转换
print("钱包里还剩下："+str(wallet)+"这么多钱")

wallet -= 10
# 等效于下面的写法
wallet = wallet -10
print("钱包里还剩下：", wallet)

# 通过type方法查看变量的类型
print(type("我靠这教程也太基础了"))
print(type(wallet))
print(type("2131"))
print(type(78.12))

# 通过int方法，将变量转换为int类型
print(int("45"))
# 会自动去掉字符串两端的空格
print(int(" 45   "))
# 会截取整数部分，丢弃小数部分
print(int(56.12))
# 以下的写法都会报错
# print(int("12.12"))
# print(int("aaa"))

# 通过float方法，将变量转换为float类型
print(float("45"))
print(float(56.12))
print(float("12.12"))
# 以下的写法都会报错
# print(float("aaa"))

# 通过str方法，将变量转换为str类型
# 基本上任何内容都可以转化为字符串
print(str("45"))
print(float(56.12))
print(str("12.12"))
print(str("aaa"))
