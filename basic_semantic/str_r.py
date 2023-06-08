#
# @author xiashuo
# @date 2023/6/8 14:56
#


import time

for i in range(101):
    print("\r{:3}%".format(i), end=' ')
    # 线程暂停 0.1 s
    time.sleep(0.1)
