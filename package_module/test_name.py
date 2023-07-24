#
# @author xiashuo
# @date 2023/7/24 19:29
#

# run_flag 为1 表示正在自我执行，run_flag 为2 表示正在被引入执行，
run_flag = 0

if __name__ == "__main__":
    run_flag = 1
    print("i am running by myself")
else:
    run_flag = 2
    print("i am imported")

if run_flag == 1:
    print("don't want to work , want to lie down")
else:
    print("so great to work here")
