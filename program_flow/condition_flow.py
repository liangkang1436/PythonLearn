#
# @author xiashuo
# @date 2023/6/4 12:22
#

# 引入随机数类
# import random
#
# num =  random.randint(0,10)
# print(f"{num}的类型是：{type(num)}")

age = input("please enter your age:")
age_int = int(age)
if age_int < 18:
    # Python中通过缩进（一般是四个空格）来确定代码的归属（范围）
    # 这个跟Java不同，Java通过{}确定归属（范围）
    print("i am a child")
elif age_int >= 18 and age_int < 50:
    print("i am a adult ")
else:
    print("i am a old man")
# 这行语句因为缩进跟 print("i am a old man") 不同，所以不是else语句的执行范围
print("程序结束！")



if int(input("请输入你的年龄：")) < 18:
    print("i am a child")
elif int(input("请输入你的身高（cm）：")) < 170:
    print("i am a short ")
else:
    print("i am a normal adult")
print("程序结束！")



if int(input("input a num that greater than 5 :")) > 5:
    print("success")
    if int(input("input a num that greater than 200 :")) > 200:
        print("success")
    else:
        print("error")
else:
    print("error")