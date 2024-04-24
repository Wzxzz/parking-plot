import os
from config import Parameters
from fit import fitFun


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


y1 = [0.00, 47.06, 52.94, 52.94, 52.94, 82.35, 52.94, 64.71, 52.94, 64.71, 82.35, 82.35, 88.24, 76.47, 82.35, 88.24, 82.35, 58.82, 94.12, 64.71,
        82.35, 76.47, 52.94, 88.24, 70.59, 70.59, 64.71, 76.47, 70.59, 82.35, 64.71, 52.94, 52.94, 64.71, 88.24, 82.35, 70.59, 82.35, 70.59, 64.71,
        70.59, 88.24, 88.24, 88.24, 76.47, 76.47, 76.47, 64.71, 70.59, 82.35, 76.47, 94.12, 82.35, 76.47, 76.47, 88.24, 88.24, 64.71, 76.47, 82.35,
        64.71, 82.35, 70.59, 70.59, 82.35, 82.35, 52.94, 76.47, 82.35, 70.59, 70.59, 82.35, 94.12, 82.35, 94.12, 88.24, 76.47, 70.59, 76.47, 88.24]

#
# y = []
# for elem in y1_values:
#     y.append(str(elem))
#
# print(y)
#
# clear_file("mix.txt")
# for i in range(4):
#     with open("mix.txt", "a", encoding="utf-8") as h:
#         h.write("[" + ','.join(y) + "]" + "\n")
#
#
#
# with open("mix.txt", "r", encoding="utf-8") as g:
#     for line in g.readlines():
#         l = eval(line)
#         print(type(l))
#         print(l[2])

y_list = []
with open("mix.txt", "r", encoding="utf-8") as g:
    for line in g.readlines():
        l = eval(line)
        y_list.append(l)
y_list[0].insert(0, 0.00)
y_list[1].insert(0, 0.00)
y_list[2].insert(0, 0.00)
y_list[3].insert(0, 0.00)

x = list(range(1, 81))
# title = Parameters().show_args()

print(y_list)
print(x)
# fitFun(x, y1, y1, y1, y1)


