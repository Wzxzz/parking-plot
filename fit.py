import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import math
import time
from config import Parameters

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import time

# def fitFun(x_values, y1_values, y2_values, y3_values, y4_values, y5_values, y6_values, title="hello"):
#     # 二次多项式拟合函数
#     def poly2_fit(x, a, b, c):
#         return a * x**2 + b * x + c
#
#     # 用于存储拟合参数的字典
#     params_dict = {}
#
#     # 对每组数据使用二次多项式拟合
#     for i, y_values in enumerate([y1_values, y2_values, y3_values, y4_values, y5_values, y6_values], start=1):
#         params_poly2, covariance_poly2 = np.polyfit(x_values, y_values, 2, cov=True)
#         params_dict[f'Group {i}'] = params_poly2
#         print(f"二次多项式拟合参数（Group {i}）：", params_poly2)
#
#     x_fit = np.linspace(min(x_values), max(x_values), 100)
#
#     plt.figure(figsize=(10, 6))
#     plt.title(title, fontdict={'family': 'Times New Roman', 'size': 18})
#     plt.xlabel('x', fontdict={'family': 'Times New Roman', 'size': 18})
#     plt.ylabel('y', fontdict={'family': 'Times New Roman', 'size': 18})
#     plt.tick_params(labelsize=13)
#
#     # 绘制拟合曲线和原始数据点
#     colors = ['green', 'blue', 'black', 'red', 'orange', 'yellow']
#     labels = ['0', '5', '10', '20', '30', '50']
#     for i, (label, color) in enumerate(zip(labels, colors), start=1):
#         a, b, c = params_dict[f'Group {i}']
#         y_fit = poly2_fit(x_fit, a, b, c)
#         plt.plot(x_fit, y_fit, label=label, color=color)
#         plt.plot(x_values, eval(f'y{i}_values'), label = label, color=color, alpha=0.1)
#
#
#     plt.legend(labels, prop={'family': 'Times New Roman', 'size': 16})
#     # plt.show()
#     now = time.strftime('%m-%d_%H%M')  # 结构化输出当前的时间
#     plt.savefig("mix/mynet_1/lr0.001,ep80,bs4/"+str(now)+".png")
#     plt.clf()
#

def fitFun(x_values, y1_values, y2_values, y3_values, y4_values, y5_values, y6_values, title="hello"):

    def poly2_fit(x, a, b, c):
        return -a * np.exp(b * (-x)) + c
    # def poly2_fit(x, a, b, c):
    #     return a * x**2 + b * x + c

    # 指数函数
    params_exp1, covariance_exp = curve_fit(poly2_fit, x_values, y1_values)
    a, b, c = params_exp1
    print("指数拟合参数：", a, b, c)

    # 指数函数
    params_exp2, covariance_exp = curve_fit(poly2_fit, x_values, y2_values)
    a, b, c = params_exp2
    print("指数拟合参数：", a, b, c)

    # 指数函数
    params_exp3, covariance_exp = curve_fit(poly2_fit, x_values, y3_values)
    a, b, c = params_exp3
    print("指数拟合参数：", a, b, c)

    # 指数函数
    params_exp4, covariance_exp = curve_fit(poly2_fit, x_values, y4_values)
    a, b, c = params_exp4
    print("指数拟合参数：", a, b, c)


    # 指数函数
    params_exp5, covariance_exp = curve_fit(poly2_fit, x_values, y5_values)
    a, b, c = params_exp5
    print("指数拟合参数：", a, b, c)

    # 指数函数
    params_exp6, covariance_exp = curve_fit(poly2_fit, x_values, y6_values)
    a, b, c = params_exp6

    print("指数拟合参数：", a, b, c)

    x_fit = np.linspace(min(x_values), max(x_values), 100)
    # 指数函数
    a1, b1, c1 = params_exp1
    a2, b2, c2 = params_exp2
    a3, b3, c3 = params_exp3
    a4, b4, c4 = params_exp4
    a5, b5, c5 = params_exp5
    a6, b6, c6 = params_exp6
    y1_fit = poly2_fit(x_fit, a1, b1, c1)
    y2_fit = poly2_fit(x_fit, a2, b2, c2)
    y3_fit = poly2_fit(x_fit, a3, b3, c3)
    y4_fit = poly2_fit(x_fit, a4, b4, c4)
    y5_fit = poly2_fit(x_fit, a5, b5, c5)
    y6_fit = poly2_fit(x_fit, a6, b6, c6)

    plt.figure(1)
    plt.title(title, fontdict={'family': 'Times New Roman', 'size': 18})
    plt.xlabel('x', fontdict={'family': 'Times New Roman', 'size': 18})
    plt.ylabel('y', fontdict={'family': 'Times New Roman', 'size': 18})
    plt.ylabel('y', fontdict={'family': 'Times New Roman', 'size': 18})
    plt.ylabel('y', fontdict={'family': 'Times New Roman', 'size': 18})
    plt.ylabel('y', fontdict={'family': 'Times New Roman', 'size': 18})
    plt.tick_params(labelsize=13)

    plt.plot(x_fit, y1_fit, label="0", color='green')   # 0
    plt.plot(x_fit, y2_fit, label="5", color='blue')   # 5
    plt.plot(x_fit, y3_fit, label="10", color='black')  # 10
    plt.plot(x_fit, y4_fit, label="20", color='red')  # 20
    plt.plot(x_fit, y5_fit, label="30", color='orange')  # 30
    plt.plot(x_fit, y6_fit, label="50", color='yellow')   # 50

    plt.plot(x_values, y1_values, label="0", color='green', alpha=0.1)  # 0 5 10 15 20 25 30
    plt.plot(x_values, y2_values, label="5", color='blue', alpha=0.1)  # 5
    plt.plot(x_values, y3_values, label="10", color='black', alpha=0.1)  # 10
    plt.plot(x_values, y4_values, label="20", color='red', alpha=0.1)  # 20
    plt.plot(x_values, y5_values, label="30", color='orange', alpha=0.1)  # 30
    plt.plot(x_values, y6_values, label="50", color='yellow', alpha=0.1)  # 50

    plt.legend(['0', '5', '10', '20', '30', '50'], prop={'family': 'Times New Roman', 'size': 16})
    # plt.show()
    now = time.strftime('%m-%d_%H%M')  # 结构化输出当前的时间
    plt.savefig("mix/"+str(now)+".png")
    plt.clf()



