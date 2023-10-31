#
# 博客同步到阿里云的工具，打包成 exe 的方式为，在当前脚本所在路径下执行 pyinstaller -F -w -i sync.ico sync.py，然后 dist 目录下的就是此脚本打包出来的 exe 文件
# @author xiashuo
# @date 2023/10/7 10:35
#
import subprocess
import os
from datetime import datetime
import autocorrect_py as autocorrect

# 如果是 0 则表示只在没有设置前言的时候才加上前言，如果是 1 则表示每次执行都更新前言，这会修改文件，使得文件的修改时间更新
# 如果更新前言，也会同时进行文档格式化
always_update_front_matter = 0


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
                # 4. 更新图片地址
                update_image_url(file_path)

                # 5. 格式化文件 - 添加必要的空格
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


def update_image_url(file_path):
    # 1. 读取文件
    f = open(file_path, 'r+', encoding="UTF-8")
    all_the_lines = f.readlines()
    # 2. 清空
    f.seek(0)
    f.truncate()
    for line in all_the_lines:
        # 3. 更新图片地址，写入文件中
        line = line.replace("![](https://cdn.jsdelivr.net/gh/liangkang1436/image-hosting@main/picgo-images/",
                            "![](https://lk-images.oss-cn-beijing.aliyuncs.com/images/")
        line = line.replace("src=\"https://cdn.jsdelivr.net/gh/liangkang1436/image-hosting@main/picgo-images/",
                            "src=\"https://lk-images.oss-cn-beijing.aliyuncs.com/images/")
        f.write(line)
    f.close()


def format_file(file_path, file_name):
    f = open(file_path, 'r+', encoding="UTF-8")
    content = f.read()
    f.seek(0)
    f.truncate()
    content = autocorrect.format_for(content, file_name)
    f.write(content)
    f.close()


def generate_blog(fresh=False):
    if fresh:
        subprocess.Popen("rmdir /s /q public", shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT, cwd="D:/Hugo/sites/xiashuo")
    subprocess.Popen("hugo", shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                     cwd="D:/Hugo/sites/xiashuo")


def invoke_rsync():
    # 执行命令
    # 注意，命令必须是全路径
    rsync_command = "D:/cwRsync/cwrsync_6.2.9_x64_free/bin/rsync.exe -az --port 8730 --delete --password-file=/cygdrive/D/cwRsync/password.txt --exclude-from=/cygdrive/D/cwRsync/exclude.txt /cygdrive/D/Hugo/sites/xiashuo/public/ root@xiashuo.xyz::blog/"
    # pyinstaller 如果带有 -w 参数，则必须指定 shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT 这一串参数
    process = subprocess.Popen(rsync_command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                               stderr=subprocess.STDOUT)
    # process.wait()


if __name__ == '__main__':
    # 0. 获取当前目录
    current_path = os.getcwd()
    # 1. 递归格式化当前目录下所有的 md 文件
    format_files(current_path)
    # 2. 重新生成博客
    generate_blog(False)
    # 3. 同步到阿里云
    invoke_rsync()
