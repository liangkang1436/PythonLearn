#
# markdown 文档格式化工具，打包成 exe 的方式为，在当前脚本所在路径下执行 pyinstaller -F -w -i format-brush.ico markdown_formatter.py，然后 dist 目录下的就是此脚本打包出来的 exe 文件
# @author xiashuo
# @date 2023/9/20 7:33
#
import os
from datetime import datetime
import autocorrect_py as autocorrect

# 如果是 0 则表示只在没有设置前言的时候才加上前言，如果是 1 则表示每次执行都更新前言，这会修改文件，使得文件的修改时间更新
# 如果更新前言，也会同时进行文档格式化
always_update_front_matter = 1

def format_files(dirPath):
    for root, dirs, files in os.walk(dirPath):
        for file_name in files:
            if file_name.startswith("_index"):
                continue
            if not file_name.endswith(".md"):
                continue
            file_path = os.path.join(root, file_name)
            # 1. 准备文件更新时间
            file_attr = os.stat(file_path)
            ctime = datetime.fromtimestamp(file_attr.st_ctime).strftime("%Y-%m-%dT%H:%M:%S%z+08:00")
            # 更新时间动态获取
            mtime = datetime.fromtimestamp(file_attr.st_mtime).strftime("%Y-%m-%dT%H:%M:%S%z+08:00")

            # 2. 获取文章的标题
            title = get_file_title(file_path)

            # 3. 更新前言
            has_update = set_front_matter(file_path, ctime, title)

            if has_update == 1:
                # 4. 格式化文件 - 添加必要的空格
                format_file(file_path, file_name)

        for dir in dirs:
            now_path = os.path.join(root, dir)
            format_files(now_path)


def get_file_title(file_path):
    title = ""
    f = open(file_path, 'r+', encoding="UTF-8")
    all_the_lines = f.readlines()
    for line in all_the_lines:
        if line.startswith("# "):
            title = line.replace("# ", "").strip()
            break
    f.close()
    return title


def set_front_matter(file_path, ctime, title):
    frontmatter = ["+++\n", "title = '" + title + "'\n", "date = '" + ctime + "'\n", "+++\n"]
    # 1. 获取旧的前言的行号范围
    f = open(file_path, 'r+', encoding="UTF-8")
    all_the_lines = f.readlines()
    frontmatter_start = -1
    frontmatter_end = -1
    i = -1
    for line in all_the_lines:
        i = i + 1
        if frontmatter_start == -1 and line.startswith("+++"):
            frontmatter_start = i
            continue
        if frontmatter_start != -1 and line.startswith("+++"):
            frontmatter_end = i
            break
    f.close()

    if always_update_front_matter == 1 or frontmatter_start == -1:
        # 2. 再次读取文件
        f = open(file_path, 'r+', encoding="UTF-8")
        all_the_lines = f.readlines()
        # 3. 清空
        f.seek(0)
        f.truncate()
        # 4. 去掉旧前言，拼接上新的前言
        all_the_lines = all_the_lines[(frontmatter_end + 1):]
        all_the_lines = frontmatter + all_the_lines
        # 5. 写入文件中
        for line in all_the_lines:
            f.write(line)
        f.close()
        # 更新前言返回 1
        return 1
    # 不更新前言，返回 0
    return 0


def format_file(file_path, file_name):
    f = open(file_path, 'r+', encoding="UTF-8")
    content = f.read()
    f.seek(0)
    f.truncate()
    content = autocorrect.format_for(content, file_name)
    f.write(content)
    f.close()


if __name__ == '__main__':
    current_path = os.getcwd()
    # print(current_path)
    format_files(current_path)
