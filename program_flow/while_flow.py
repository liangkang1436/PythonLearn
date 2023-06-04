#
# @author xiashuo
# @date 2023/6/4 15:31
#

# 计算 1 到 100 的和
sum = 0
i = 1
while i <= 100:
    sum += i
    i += 1
print(f"amount is {sum}")

# 这个import语句有点像在Java的一个类中引入另一个类
import random

# 目标数字
# 获取 1 -10 的随机数
target_num = random.randint(0, 10)
print(f"target num is {target_num}")
# 总共猜5次
action_account = 3
guess_count = 0

while guess_count < action_account:
    guess_count += 1
    if int(input("请输出目标数字：")) != target_num:
        print("猜错了")
    else:
        print("猜对了")
        break
print(f"总共猜了{guess_count}次")

# while的嵌套 输出九九乘法表
outer_count = 9
outer_index = 1
while outer_index <= outer_count:
    inner_index = 1
    while inner_index <= outer_index:
        print(f"{outer_index}*{inner_index}={outer_index * inner_index}\t", end="")
        inner_index += 1
    # 默认就是输出一个换行
    print()
    # 这是两个换行，换两行
    # print("\n")
    outer_index += 1
print("输出结束")
