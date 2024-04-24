'''此程序为自动化运行脚本，方便自动修改参数以训练网络'''

import datetime
import os
import threading
import time
import os
from fit import fitFun
from config import Parameters


def clear_file(filename):
    # 获取当前工作目录
    current_dir = os.getcwd()

    try:
        # 关闭所有与该文件相关联的进程（如果存在）
        filepath = os.path.join(current_dir, filename)

        if os.path.exists(filepath):
            tempname = "temp_" + filename

            # 重命名文件为临时文件
            os.rename(filepath, os.path.join(current_dir, tempname))

            # 删除原始文件
            os.remove(os.path.join(current_dir, tempname))

            print("成功清空文件！")
        else:
            print("指定的文件不存在！")
    except Exception as e:
        print("发生错误：", str(e))


def execCmd(cmd):
    try:
        print("命令%s开始运行%s" % (cmd, datetime.datetime.now()))
        os.system(cmd)
        print("命令%s结束运行%s" % (cmd, datetime.datetime.now()))
    except:
        print('%s\t 运行失败' % (cmd))


if __name__ == '__main__':

    print('开始时间：{}'.format(time.strftime('%m-%d_%H%M')))
    start_time = time.time()

    # 是否需要并行运行
    if_parallel = False   # 显存较小，串行比较合适

    # 需要执行的命令列表，按需求修改即可
    cmds = [
        # 'python train_real.py --task=W --weather=mix',
        # 'python train_real.py --task=P --weather=mix',
        # 'python train_real.py --task=P --weather=foggy',
        # 'python train_real.py --task=P --weather=rainy',
        # 'python train_real.py --task=P --weather=snowy',
        # 'python train_real.py --task=W --weather=mix --model=mynet',
        # 'python train_real.py --task=P --weather=mix --model=mynet',
        'python train_real.py --task=P --weather=foggy --model=mynet',
        # 'python train_real.py --task=P --weather=rainy --model=mynet',
        # 'python train_real.py --task=P --weather=snowy --model=mynet',
    ]

    learnList = [
        " --learning_rate=0.00001",
        # " --learning_rate=0.001",
        # " --learning_rate=0.001",


        # " --learning_rate=0.0001",
        # " --learning_rate=0.00001",
        # " --learning_rate=0.000001",
    ]

    mixList = [
        " --mixNum=0",
        " --mixNum=5",
        " --mixNum=10",
        " --mixNum=20",
        " --mixNum=30",
        " --mixNum=50",
    ]

    if if_parallel:
        # 并行
        threads = []
        for cmd in cmds:
            th = threading.Thread(target=execCmd, args=(cmd,))
            th.start()
            threads.append(th)

        # 等待线程运行完毕
        for th in threads:
            th.join()
    else:
        # 串行
        for cmd in cmds:

            for learning_rate in learnList:

                clear_file('mix.txt')
                for mix_num in mixList:
                    # 调用函数清空文件
                    try:
                        print("命令%s 开始运行: %s" % (cmd, datetime.datetime.now().strftime('%Y-%m-%d_%H:%M:%S')))
                        os.system(cmd+mix_num+learning_rate)
                        print("命令%s 结束运行: %s\n" % (cmd, datetime.datetime.now().strftime('%Y-%m-%d_%H:%M:%S')))
                    except:
                        print('%s\t 运行失败' % (cmd))

                y_list = []
                with open("mix.txt", "r", encoding="utf-8") as g:
                    for line in g.readlines():
                        l = eval(line)
                        y_list.append(l)
                y_list[0].insert(0, 0.00)
                y_list[1].insert(0, 0.00)
                y_list[2].insert(0, 0.00)
                y_list[3].insert(0, 0.00)
                y_list[4].insert(0, 0.00)
                y_list[5].insert(0, 0.00)
                x = list(range(1, Parameters.epochs+2))
                print(x)
                print(y_list)
                title = Parameters().show_args()

                fitFun(x, y_list[0], y_list[1], y_list[2], y_list[3],y_list[4],y_list[5],title="")


    end_time = time.time()
    total_time = end_time - start_time
    print('总用时: {:.0f}m {:.0f}s'.format(total_time // 60, total_time % 60))

