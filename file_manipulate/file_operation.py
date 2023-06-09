#
# @author xiashuo
# @date 2023/7/5 11:44
#

# 文件可以为绝对路径,也可以为相对路径
# file_path = "C:/Users/wwwli/Desktop/test_file.txt"
# 相对路径的起点即当前py文件所在的目录
# mode为 r 或者r+ 的时候,路径对应的文件必须存在,否则报错
# mode为 w w+ a a+ 的时候,路径对应的文件可以不存在,不存在的时候会自动创建
file_path = "./test_file.txt"
# 因为我们在编写文件的时候,使用的就是UTF-8编码,所以我们读取的时候,也要指定编码为 UTF-8
# 读取文件内容
file_test = open(file_path, mode="r", encoding="UTF-8")
# <class '_io.TextIOWrapper'>
print(type(file_test))
# 从当前指针所在位置开始，将后面的所有的数据都读取到一个列表中
# 每一个元素表示文件中的一行内容
content_list = file_test.readlines()
# print(content_list)
# for 循环遍历
for line in content_list:
    print(line, end="")

print()
# close() 方法用于关闭一个已打开的文件。关闭后的文件不能再进行读写操作， 否则会触发 ValueError 错误。 close() 方法允许调用多次。
# 当 file 对象，被引用到操作另外一个文件时，Python 会自动关闭之前的 file 对象。 使用 close() 方法关闭文件是一个好的习惯。
# close在最终关闭文件对象之前，会自动调用flush方法
# 文件对象最后需要关闭
file_test.close()

print("-----------")
# 其实可以直接将文件对象拿来循环，感觉是自动调用了文件对象的readlines方法
# 但是这有一个问题啊，怎么关闭文件对象呢？
# 此时 文件对象未关闭
for line in open(file_path, mode="r", encoding="UTF-8"):
    print(line, end="")

print()
print("-----------")

# with open 语法，可以自动帮我们关闭文件对象，防止我们忘记
with open(file_path, mode="r", encoding="UTF-8") as file_handler:
    content = file_handler.read()
    print(content, type(content))

print("-----------")


# 如果文件比较大，我们可以使用生成器，
def file_iterator(file_obj):
    while True:
        # readline() 方法用于从文件当前指针所在位置开始读取整行，包括 换行符（可以用字符串的strip方法去除）。如果指定了一个非负数的参数，则返回指定大小的字节数，其中换行符也算字节数
        # 已经读取了最后一行之后，在调用此方法，会返回空字符串，并且一直调用，一直返回空字符串
        line_str = file_obj.readline()
        # 空字符串 '' ，作为条件表达式，会被bool()转化为 Boolean，结果为 False
        if line_str:
            yield line_str
        else:
            # 抛出 StopIteration
            return


file_obj = open(file_path, mode="r", encoding="UTF-8")
line_reader = file_iterator(file_obj)
print(next(line_reader))
print(next(line_reader))

for line in line_reader:
    print(line, end="")

print()
file_obj.close()

print("--------------------------------")

# 查看文件读取到哪里了
# 读写文件的时候，有一个指针标识我们当前在哪里，所有的读写操作都是从当前位置开始的
# tell() 方法返回文件的当前位置，即文件指针当前位置, 它是从文件开头开始算起的字节数。
# 常见字符的字节数
# 一个数字字符算1个字节，
# 一个字母字符算1个字节，
# 一个换行符算两个字节，在Windows中占两个字节，在Linux中占一个字节
# 一个中文字符算3个字节,这个跟Java不一样,Java中一个中文字符占用2个字节
#
# 文件内容为 Python真棒
file_path_char = "./char_test.txt"
char_file = open(file_path_char, mode="r", encoding="UTF-8")
print(char_file.readline())
# 整个文件就一行, 调用一次 readline就读完了, 所以当前的位置可以算出来, 6*6 + 2*3 12个字节
print(char_file.tell())
# 在不带b的模式下,可以使用seek() 方法,但是 offset 参数必须是 0
# 回到开头,可以继续读第一行
char_file.seek(0, 0)
# read() 方法用于从文件中当前指针所在位置开始读取指定的字符数（文本模式 t）或字节数（二进制模式 b），如果未给定参数 size 或 size 为负数则读取文件所有内容到一个字符串中。size默认为 -1
# 输出从当前指针开始的6的字符,也就是输出 Python
print(char_file.read(6))
char_file.seek(0, 1)
print(char_file.readline())
char_file.seek(0, 2)
print(char_file.readline())

print("--------------------------------")

# seek() 方法用于移动文件读取指针到指定位置。
# f.seek(offset, from_what) 函数。
# offset 需要移动偏移的字节数，表示字符个数，正数表示向后移动，负数表示向前移动
# from_what 表示相对位置, 如果是 0 表示开头, 如果是 1 表示当前位置, 2 表示文件的结尾，
# 例如：
# seek(x,0) ：从起始位置即文件首行首字符开始向后移动 x 个字节
# seek(x,1) ：表示从当前位置往后移动x个字节
# seek(-x,2)：表示从文件的结尾往前移动x个字节
#
# 文件内容为 Python真棒
file_path_binary_char = "./char_binary_test.txt"
char_file = open(file_path_binary_char, mode="rb")
# rb 模式下，readline方法读出来的是字节（但是数字字符和英文字符还是原来的样子，在utf-8或者unicode编码中，字母和数字兼容 ASCII 编码，所以没有编码，编码就是自身），想要展示为字符串，需要解码
# b'Python\xe7\x9c\x9f\xe6\xa3\x92'
print(char_file.readline())
# 输出 12
print(char_file.tell())
# 回到开头
char_file.seek(0, 0)
# 然后移动到倒数 2个中文字符,和3个英文字符,也就是9个字节
char_file.seek(-9, 2)
# 再向后移动3个英文字符,也就是3个字节
char_file.seek(3, 1)
# read() 方法用于从文件读取指定的字符数（文本模式 t）或字节数（二进制模式 b），如果未给定参数 size 或 size 为负数则读取文件所有内容。默认为 -1
# 输出从当前指针开始的6个字节,也就是两个中文字符,输出 真棒 对应的字节
binary_read = char_file.read(6)
# b'\xe7\x9c\x9f\xe6\xa3\x92' <class 'bytes'>
print(binary_read, type(binary_read))
# 输出 编码为中文:真棒
print("编码为中文:" + binary_read.decode('utf-8', ))
# 在使用带b的模式的时候,要将字节解码为中文的时候,很有可能因为会因为字节不完整,导致无法解码,比如真棒这两个字总共6个字节,结果字节对象里只有5个字节,那这样进行解码的时候就会报错
# 为了不报错,我们可以指定errors参数 decode(encoding='utf-8', errors='ignore'),这样,当无法解码的时候,就不会报错
print("--------------------------------")

# 写
# mode为 r 或者r+ 的时候,路径对应的文件必须存在,否则报错
# mode为 w w+ a a+ 的时候,路径对应的文件可以不存在,不存在的时候会自动创建
file_path_write = "./write_test.txt"
file_write = open(file_path_write, mode="w", encoding="UTF-8")
for i in range(0, 10):
    # write() 方法用于向文件中写入指定字符串。
    # 在文件关闭前或缓冲区刷新前，字符串内容存储在缓冲区中，这时你在文件中是看不到写入的内容的。
    # 如果文件打开模式带 b，那写入文件内容时，str (参数)要用 encode 方法转为 bytes 形式，否则报错：TypeError: a bytes-like object is required, not 'str'。
    file_write.write(str(i) + "\n")

line_list = ["批量插入1\n", "批量插入2\n", "批量插入3\n", "批量插入4\n"]
# writelines() 方法用于向文件中写入一序列的字符串。
# 这一序列字符串可以是由迭代对象产生的，如一个字符串列表。
# 换行需要制定换行符 \n。
file_write.writelines(line_list)

# flush() 方法是用来刷新缓冲区的，即将缓冲区中的数据立刻写入文件，同时清空缓冲区，不需要是被动的等待输出缓冲区写入。
# 一般情况下，文件关闭后会自动刷新缓冲区，但有时你需要在关闭前刷新它，这时就可以使用 flush() 方法。
file_write.flush()

file_write.close()

# 缓冲策略
file_path_write_buffer = "./write_buffer_test.txt"
# buffering=1 行缓存
# 如果模式为a,则会一直追加
file_write_buffer = open(file_path_write_buffer, mode="a", encoding="UTF-8", buffering=1)
# 使用write()方法写入文件的时候，只要写入的内容中包含换行符`\n`，就相当于在write()方法后调用了一次flush()方法
file_write_buffer.write("1111")
file_write_buffer.write("222\n")
file_write_buffer.write("333")
file_write_buffer.write("444\n")
file_write_buffer.write("55555")
file_write_buffer.write("666\n777777")
file_write_buffer.write("88888")
file_write_buffer.flush()
file_write_buffer.close()

file_path_write_buffer_2 = "./write_buffer_test_2.txt"
# buffering > 1 的缓存设置
# 仅在二进制模式下能生效，文本模式下不生效，虽然官方文档没说，但是我测试出来是这样的
file_write_buffer_2 = open(file_path_write_buffer_2, mode="wb", buffering=3)
# 超过3个字节的输入，都会直接写入到物理文件中
file_write_buffer_2.write("我靠".encode("UTF-8"))
file_write_buffer_2.write("8888".encode("UTF-8"))
file_write_buffer_2.write("111\n".encode("UTF-8"))
file_write_buffer_2.flush()
file_write_buffer_2.close()

# 模式的值
# ValueError: must have exactly one of create/read/write/append mode
# file_object_test = open(file_path, mode="rbw", encoding="UTF-8", buffering=1)
