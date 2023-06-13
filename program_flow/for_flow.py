#
# @author xiashuo
# @date 2023/6/4 17:09
#


name = "xiashuo.xyz"
# 循环字符串中的字符
for i in name:
    print(f"{i}", end='')
print("-------")

# 通过range可以获取一个简单的数字序列
# 从0(包含)开始到10(不包含)
# 注意，变量类型是 <class 'range'>
print(type(range(0, 10)))
# for循环
for i in range(10):
    print(f"{i}")
print("-------")
# 从5(包含)开始到10(不包含)
for i in range(5, 10):
    print(f"{i}")
print("-------")
# 从5(包含)开始到10(不包含)，设置序列的步长（step）为2，即每隔2输出一个数字，默认的step是1
for i in range(5, 10, 2):
    print(f"{i}")
print("-------")

# 如何获取被便利元素的索引呢？用 enumerate 方法即可
for inx, val in enumerate(name):
    print(f"{inx}处的元素是{val}")

# 从 3 到20，每隔5个数字输出一次
for index, ele in enumerate(range(3, 20, 5)):
    print(f"{index}: {ele}")
# 注意，在for循环的外部，访问index和ele，是可以访问到的，这一点跟Java很不一样
# 这样是违反规范的，不建议这样做
# 可以看到爆黄色警告
print(f"在for循环的外部访问for循环的内部的临时变量：{index}: {ele}")
# 如果你确实需要在for循环的外部来访问，你可以先把for循环内部需要用到的变量定义好，然后就for循环的时候会直接使用这些变量
index_new = 0
ele_new = 0
# for循环会直接使用
for index_new, ele_new in enumerate(range(3, 20, 5)):
    print(f"{index_new}: {ele_new}")
print(f"在for循环的外部访问变量：{index_new}: {ele_new}")

# 九九乘法表 for循环版本
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{i}*{j}={i * j}\t", end="")
    print()
print("输出结束")
