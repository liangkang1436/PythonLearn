#
# @author xiashuo
# @date 2023/10/22 8:55
#
import os


def format_files(dirPath):
    for root, dirs, files in os.walk(dirPath):
        for file_name in files:
            if file_name.startswith("_index"):
                continue
            if not file_name.endswith(".md"):
                continue
            file_path = os.path.join(root, file_name)

            # 3. 更新图片 URL
            update_image_url(file_path)

        for dir in dirs:
            now_path = os.path.join(root, dir)
            format_files(now_path)


def update_image_url(file_path):
    # 1. 读取文件
    f = open(file_path, 'r+', encoding="UTF-8")
    all_the_lines = f.readlines()
    # 2. 清空
    f.seek(0)
    f.truncate()
    for line in all_the_lines:
        # 3. 更新图片地址，写入文件中
        line = line.replace("![](https://cdn.jsdelivr.net/gh/liangkang1436/image-hosting@main/picgo-images/","![](https://lk-images.oss-cn-beijing.aliyuncs.com/images/")
        f.write(line)
    f.close()


if __name__ == '__main__':
    current_path = os.getcwd()
    # print(current_path)
    format_files(current_path)
