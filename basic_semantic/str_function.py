#
# @author xiashuo
# @date 2023/6/9 16:35
#

str_now = "abcdefg13456"

print("------------------------------字符串中的内部函数----------------------------------")
print("----大小写相关----")
# 首字母大写
print(str_now.capitalize())

# 返回一个不大小写不敏感的字符串用于对比
# 效果跟 lower 有点像
print("ABcdEFG123456".casefold())

# 全大写
# 输出 ABCDEFG
print("abcdefg".upper())
# 全小写
# 输出 abcdefg
print("ABCDEFG".lower())
# 大小写反转
# 输出 abCDEfg
print("ABcdeFG".swapcase())

# 将每一个单词的首字母大写，每一个单词除首字母以外的字母小写，
# 这个叫title case 还挺有意思的
print("this is my life".title())
print("tHis iS mY liFe".title())

print("----格式化相关----")

# 格式化，我们前面已经了解过了
print('姓名是 {name}，年龄是 {age}'.format(name='Tom', age=20))
# 参数类型必须是字典，没有format方法灵活
print("myname is {name}".format_map({"name": "xiashuo"}))

# 在字符串左边补零，将字符串补足到指定长度
print("python".zfill(15))

# 居中对齐
# 将字符串内容放到指定长度的中间，可以指定左右填充字符，默认使用空格
# 输出"  python  "
print("python".center(10))
# 输出"**python**"
print("python".center(10, "*"))

# 左对齐
print("python".ljust(10, "*"))

# 右对齐
print("python".rjust(10, "*"))

# tab 符号 \t 默认的列宽是8个字符，如果一列的内容宽度不到8，会用空格补齐，如果超过了一倍的列宽，那就会按照两倍的列宽补齐空格，以此类推
# 默认列宽8个字符
# 输出
# python  Java    C++
# python1 Java1   C++1
print("python\tJava\tC++\npython1\tJava1\tC++1".expandtabs())
# 我们可以指定列宽为任意个字符
# python      Java        C++
# python1     Java1       C++1
print("python\tJava\tC++\npython1\tJava1\tC++1".expandtabs(12))

print("----编码/解码----")
# 字符串的编解码
str_encode = "我的天空".encode(encoding="utf-8", errors="strict")
print(str_encode)
str_decode = str_encode.decode(encoding="utf-8", errors="strict")
print(str_decode)

print("----前缀/后缀的处理----")

# 是否以字符串开头
print("abcdefg".startswith("abc"))
# 可以指定匹配的多个字符串，用元组传入
print("abcdefg".startswith(("1", "abc")))
# 可以指定起点和终点索引
print("0123abcdefg".startswith(("123", "abc"), 1, 6))
# 长度不够，导致匹配不到
print("0123abcdefg".startswith(("123", "abc"), 1, 3))

# 是否以字符串结束
print("abcdefg".endswith("efg"))
# 可以指定匹配的多个字符串，用元组传入
print("abcdefg".endswith(("1", "efg")))
# 可以指定起点和终点索引
print("abcdefg01230".endswith(("123", "abc"), -6, -1))
# 长度不够，导致匹配不到
print("0123abcdefg".endswith(("123", "abc"), -2, -1))

# 删除字符串头尾的指定字符，即，删除指定前缀后缀，如果不指定，那就是删除空格
python_str = "   python   "
strip_result = python_str.strip()
# 注意，原字符串是不会变化的，返回的是出来之后的结果
print(python_str)
print(strip_result)
# 如果指定了字符串，会按照指定字符串中的所有字符来删除前缀后缀
# 输出 ython 字符串头部的 aaap 和尾部的 bbb 被删除
print("aaapythonbbb".strip("abp"))
# 只删除前缀
# 输出 ythonaa
print("aaapythonaa".lstrip("abpn"))
# 只删除后缀
# 输出 aaapytho
print("aaapythonaa".rstrip("abpn"))

# 移除前缀，效果类似于 string[len(prefix):] 效果等同于 lstrip
print("aaa_python".removeprefix("aa"))
# 移除后缀 效果等同于 rstrip
print("python_bbb".removesuffix("bb"))

print("----拼接----")
# 分隔符调用join，join方法的参数是列表或者字典或者元组或者集合
print("&&".join(["a", "b", "c", "d"]))
print("&&".join(("a", "b", "c", "d")))
print("&&".join({"a", "b", "c", "d"}))
print("&&".join({"a": "1", "b": "2", "c": "3", "d": "4"}))
# 输出都是a&&b&&c&&d


print("----翻译(替换)----")
# 如果只有一个参数，它必须是一个将Unicode序数(整数)或字符映射为Unicode序数、字符串或None的字典。然后将字符键转换为序号。
# 如果有两个参数，它们必须是长度相等的字符串，那样在结果字典中，x中的每个字符将被映射到y中相同位置的字符。如果有第三个参数，它必须是一个字符串，其字符将被映射到结果中的None。
# table_1 和 table_2 的效果相同
table_1 = str().maketrans({"t": "1", "h": "2", "i": "3", "s": "4", ".": None, "p": None, "y": None})
# 一般我们用这种方式，比较方便
table_2 = str().maketrans("this", "1234", ".py")
print(table_1)
print(table_2)
str_2_trans = "this is string example....wow!!! py"
# translate 方法处理的是原字符串的副本，并不会修改源字符串
print(str_2_trans.translate(table_1))
print(str_2_trans.translate(table_2))
# 源字符串没有修改

# replace 替换方法，不支持正则表达式
# 移除字符串中的空格
print("p y t h o n".replace(" ", ""))
# 只替换头两个"aa"，再有多的也不管了
print("pyaataahaaobbn".replace("aa", "", 2))


# 好像没有从右边开始替换的方法，那我们就自己实现一个
def right_replace(string, old, new, max=1):
    return string[::-1].replace(old[::-1], new[::-1], max)[::-1]


print(right_replace("pyaataahaaobbn", "aa", "", 2))

print("----分割（小段分割）----")

# 传入分隔符，将字符串分为三部分，分隔符之前的部分、分隔符自身、分隔符后面的部分，用这三个部分按顺序组成元组返回
# 如果没找到分隔符，返回的元组的第一个元素就是字符串本身，然后后面两个字符串都是空
# 注意，如果字符串中存在多个分隔符，只会按照第一个分隔符所在的位置分割，忽略后续的分隔符，
# 即 partition 最终的结果，一定是一个包含三个字符串元素的元组
# 返回('py', 'th', 'on')
print("python".partition("th"))
# 返回('python', '', '')
print("python".partition("ths"))
# 注意，如果字符串中存在多个分隔符，只会按照第一个分隔符所在的位置分割，忽略后续的分隔符，
# 返回('1111', ';', '2222;3333;4444')
print("1111;2222;3333;4444".partition(";"))
# 当然，我们也可以从右边开始找分隔符，找到之后以其为分割点做分割
# 返回('1111;2222;3333', ';', '4444')
print("1111;2222;3333;4444".rpartition(";"))

# 通过分隔符将字符串分割为多份，
# 第一个参数是分隔符，如果不设置，也就是None，那就会以空格或者空白进行分割，包括\\n \\r \\t \\f 这些转义字符，同时如果分割出的部分是空字符串，则会将其丢弃，最终的效果就像是分隔符好像是任意宽度的空格
# 第二个参数是最大分割次数(从左边开始)。-1(默认值)表示没有限制。0表示不分割，直接返回整个字符串，1表示分割一次，字符串被分割为两段，返回的结果列表的最大索引是1，2表示分割两次，字符串被分割为三段，返回的结果列表的最大索引是2，以此类推
print("111 222 333 444 555".split())
# 最终的效果就像是分隔符好像是任意宽度的空格
print("111     222     333    444   555".split())
print("111 \t 222 \t333 \t444\t555".split())
# 返回['1', '2', '3', '4', '5', '6', '7', '8', '9']
print("1;2;3;4;5;6;7;8;9".split(";"))
# 返回['1', '2', '3', '4', '5', '6', '7', '8;9']
print("1;2;3;4;5;6;7;8;9".split(";", 7))
# 当然，我们也可以从右边开始分割
# 返回['1;2', '3', '4', '5', '6', '7', '8', '9']
print("1;2;3;4;5;6;7;8;9".rsplit(";", 7))

# 按照换行来拆分字符串 只要是能换行符号的都会被采纳为分隔符
str_multiple_line = """aaa
bbb
ccc
ddd
eee
ffff
"""
# 输出['aaa', 'bbb', 'ccc', 'ddd', 'eee', 'ffff']
print('"""', str_multiple_line.splitlines())
# \n 会被拆分
str_multiple_line_3 = "1111\n222\n333"
print("\\n", str_multiple_line_3.splitlines())
# \f 会被拆分
str_multiple_line_3 = "1111\f222\f333"
print("\\f", str_multiple_line_3.splitlines())
# \v 会被拆分
str_multiple_line_3 = "1111\v222\v333"
print("\\v", str_multiple_line_3.splitlines())
# 如果参数为True，会把分隔符也带在后面
str_multiple_line_4 = "1111\n222\n333"
print("\\n with delimiter", str_multiple_line_4.splitlines(True))

print("----统计相关----")

str_temp = "aaa124556aaa123aaa"
# 在指定的范围内查找特定字符串出现的次数
# 不指定范围的话就是全部字符
print(str_temp.count("aaa"))
print(str_temp.count("123"))
# 指定范围为 0-9
print(str_temp.count("aaa", 0, 9))

print("----查找相关----")

# 查询指定字符串在特定范围内第一次出现的位置
# 不指定范围的话就是全部字符
# 没找到就报错
print(str_temp.index("12"))
print(str_temp.index("12", 10, 19))
# ValueError: substring not found
# print(str_temp.index("1#"))
# 查询指定字符串在特定范围内最后一次出现的位置
# 不指定范围的话就是全部字符
print(str_temp.rindex("aaa"))

# 跟 index 方法功能完全相同，
# 唯一的区别就是 index方法找不到的时候直接报错，find犯法找不到的时候返回 -1，
print(str_temp.find("12"))
print(str_temp.find("12", 10, 19))
print(str_temp.rfind("aaa"))

print("----判断相关----")

# 是否是字母和数字组成的字符串
print("12fd".isalnum())
print("12fd@@".isalnum())

# 是否每个字符都是字母或者中文字符
print("dfasdfa".isalpha())
print("dfasdfa121".isalpha())
# 中文字符 isalpha 返回true
print("中文字符", "中文字符".isalpha())

# 是否字符串中的字符都是数字
# 注意要跟能否转化为数字进行区分
print("121".isnumeric())
# 小数会返回False，因为 . 不是数字
print("121.2".isnumeric())
print("dfasdfa".isnumeric())

# 是否每个字符都是 ascii 字符
# 键盘上能敲出来的特殊符号都是 ascii 字符
print("+/!@#".isascii())
# 26个英文字母也是 ascii 字符
print("abcdefg".isascii())
# 但是汉字不是ascii 字符，中文输入法下的符号比如！，也不是ascii 字符，其它语言的文字也不是
print("我￥！".isascii())
# 关于什么是ascii 字符，请看 http://c.biancheng.net/c/ascii/ 中的表格的 字符/缩写 这一列

# 是否每个字符都是 数字 ，跟 isnumeric 好像没有区别
print("123456".isdigit())
# . 不是数字
print("123.456".isdigit())
print("ADCD".isdigit())

# 是否每个字符都是 十进制 数字 ，跟 isnumeric 好像没有区别
print("1213".isdecimal())
# 0x 都是16进制字符
print("0x1213", "0x1213".isdecimal())

# 字符串是关键字
print("def".isidentifier())
print("class".isidentifier())
# 1213不是关键字
print("1213".isidentifier())

# 是否每个字符都是 小写
print("dfasdfa".islower())
print("DFASDFA".islower())

# 是否每个字符都是 大写
print("DFASDFA".isupper())
print("dfasdfa".isupper())

# 是否每个字符都是 空格
print(" ".isspace())
print("   ".isspace())
# 基本上这些转义字符都是空格
print("\t".isspace())
print("\f".isspace())
print("\n".isspace())
print("\f".isspace())
print("\r".isspace())

"""
8个不可打印字符\cx，\f，\n，\r，\s，\S，\t、\v
\cx匹配由x指明的控制字符,x值必需为A-Z或a-z的大小写字符,\cA匹配一个Control-A控制字符
\f匹配一个换页符，leaf
\n匹配一个换行符，next
 \r匹配一个回车符，enter
\t匹配一个制表符，table
\v匹配一个垂直制表符，vertical
\s匹配任何空白字符，等效于[\r\n\r\t\v]
\S匹配任何非空白字符
"""
# 是否所有的字符都是可打印的
print("dfasdfasd".isprintable())
print("12\n".isprintable())

# 所有单词都是以大写开始，其余字母均为小写
print("This Is My Life".istitle())
print("this is my life".istitle())
