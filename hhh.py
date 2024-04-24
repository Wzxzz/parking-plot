import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial.polynomial import Polynomial

# 原始数据
x = np.array([0.96, 0.965, 0.97, 0.975, 0.98, 0.985, 0.99, 0.992, 0.994, 0.996, 0.998, 1.0])
y = np.array([0.9795, 0.9695, 0.9600, 0.9540, 0.9505, 0.8980, 0.8890, 0.7965, 0.7475, 0.6255, 0.5205, 0.5025])



# x = np.array([0.96, 0.965, 0.97, 0.975, 0.98, 0.985, 0.99, 0.992, 0.994, 0.996, 0.998, 1.0])
# y = np.array([0.8545, 0.8497, 0.8425, 0.8256, 0.7940, 0.7532, 0.7010, 0.6065, 0.5770, 0.5416, 0.5243, 0.5030])

split_point = 0.98

# 分段数据
x1, y1 = x[x <= split_point], y[x <= split_point]
x2, y2 = x[x >= split_point], y[x >= split_point]

# 分段拟合 - 二次多项式和五次多项式
poly2 = Polynomial.fit(x1, y1, 2)
poly5 = Polynomial.fit(x2, y2, 5)

# 生成平滑数据进行绘图
x1_smooth = np.linspace(x1.min(), x1.max(), 500)
x2_smooth = np.linspace(x2.min(), x2.max(), 500)

y1_smooth = poly2(x1_smooth)
y2_smooth = poly5(x2_smooth)

# 绘制曲线
plt.scatter(x, y, color='r')  # 原始数据点
plt.plot(x1_smooth, y1_smooth,  color='g')
plt.plot(x2_smooth, y2_smooth,  color='g')

plt.xlim(split_point, 1.0)

plt.xlabel('Concentration')
plt.ylabel('Accuracy')
plt.title(' ')
plt.legend()

plt.show()

