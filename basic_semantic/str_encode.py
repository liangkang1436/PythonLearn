#
# @author xiashuo
# @date 2023/6/27 17:07
#

# Unicode 编码相关
# 屌字的unicode码，实际上，你可以把这个认同为这就是一个汉字
# '\u'是转义字符，表示unicode编码。
char = "\u5c4c"
# 可直接输出Unicode编码对应的字符
print(char)

# 这个字符对应的Unicode编码对应的字符串
char_code_str = "\\u5c4c"
print(char_code_str)
# 首先将这个字符串进行"utf-8"编码为字节
char_byte = char_code_str.encode("utf-8")
print(char_byte, type(char_byte))
# 然后再进行Unicode解码
char_new = char_byte.decode('unicode_escape')
print(char_new, type(char_new))

# 这个过程我们也可以反向来进行，获取指定字符的Unicode编码字符串
print("屌".encode("unicode_escape").decode("utf-8"))
# 输出 A, 没有 Unicode码，其采用的是 ASCII 值为 0x39
print("z".encode("unicode_escape").decode("utf-8"))
# 输出 9, 没有 Unicode码，其采用的是 ASCII 值为 0x7A
print("9".encode("unicode_escape").decode("utf-8"))

# 字符串的比较
# 数字和字符 均采用 ASCII 编码，跟中文的比较也是直接拿 ASCII 码跟 Unicode码比较，
# 数字永远比汉字要小
# True
print("9" < "掉")
# True
print("z" < "掉")

# 汉字之间可以通过Unicode编码来比较
# \u6211
print("我".encode("unicode_escape").decode("utf-8"))
# \u7684
print("的".encode("unicode_escape").decode("utf-8"))
# True
print("我" < "的")

# 这个Java有所不同，Java中JVM会自动复用字符串对象
# True
print("我" == "我")
# True
print("我" == str("我"))

# 多位比较
# 按位比较，也就是一位位进行对比，只要有一位大，那么整体就大
# True
print("ab" > "aaaa")

