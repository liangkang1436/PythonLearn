#
# @author xiashuo
# @date 2023/6/4 11:08
#

print("please input your name")
# 会一直阻塞，直到用户在控制台输入并回车
# 用户输入的内容时绿色的
name = input("name：")
# 用户的输入最终都是字符串类型
# 输出 <class 'str'>
print(type(name))
# 回车之后继续往后执行
print(f"your name is {name}")
