#
# 博客同步到阿里云的工具，打包成 exe 的方式为，在当前脚本所在路径下执行 pyinstaller -F -w -i sync.ico rsync.py，然后 dist 目录下的就是此脚本打包出来的 exe 文件
# @author xiashuo
# @date 2023/10/7 10:35
#
import subprocess


def generate_blog(fresh=False):
    if fresh:
        subprocess.Popen("rmdir /s /q public", shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, cwd="D:/Hugo/sites/xiashuo")
    subprocess.Popen("hugo", shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, cwd="D:/Hugo/sites/xiashuo")


def invoke_rsync():
    # 执行命令
    # 注意，命令必须是全路径
    rsync_command = "D:/cwRsync/cwrsync_6.2.9_x64_free/bin/rsync.exe -az --port 8730 --delete --password-file=/cygdrive/D/cwRsync/password.txt --exclude-from=/cygdrive/D/cwRsync/exclude.txt /cygdrive/D/Hugo/sites/xiashuo/public/ root@xiashuo.xyz::blog/"
    # pyinstaller 如果带有 -w 参数，则必须指定 shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT 这一串参数
    process = subprocess.Popen(rsync_command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)


if __name__ == '__main__':
    generate_blog(True)
    invoke_rsync()
