#
# @author xiashuo
# @date 2023/7/9 10:48
#

# 文件复制
file_source = open("./copy_source.csv", "r", encoding="utf-8")
file_target = open("./copy_target.csv", "w", encoding="utf-8")
file_target.write("name,age,score,type\n")
for line in file_source:
    # 去掉两端的空格，最主要的是去掉最后的换行符
    line = line.strip()
    line_parts = line.split(",")
    if len(line_parts) < 4 or (not str(line_parts[2]).isdigit()):
        continue
    if int(line_parts[2]) >= 100 and line_parts[3] == 'prod':
        file_target.write(line + "\n")

file_source.close()
file_target.close()

# 二进制复制，比如视频
# 这里就不把视频上传到GitHub了，太大了
file_binary_source = open("F:/羽毛球打球视频/2022年09月30日/VID_20220930_184501.mp4", "rb")
file_binary_target = open("F:/羽毛球打球视频/2022年09月30日/VID_20220930_184501_复制.mp4", "wb", )

while True:
    # 一次读取2kb
    content_binary = file_binary_source.read(2048)
    # 空字节 b'' ，作为条件表达式，会被bool()转化为 Boolean，结果为 False
    if content_binary:
        file_binary_target.write(content_binary)
    else:
        break

file_binary_source.close()
file_binary_target.close()
