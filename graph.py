import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

# 原始数据
x = np.array([0.96, 0.97, 0.98, 0.99, 0.992, 0.994, 1.0])
y = np.array([0.9495, 0.9600, 0.9505, 0.8890, 0.7965, 0.7475, 0.5025])

# 创建平滑的插值曲线
x_smooth = np.linspace(x.min(), x.max(), 300)
y_smooth = make_interp_spline(x, y)(x_smooth)

# 绘制平滑曲线
plt.plot(x_smooth, y_smooth, linestyle='-', color='b')

# 绘制原始数据点
plt.scatter(x, y, marker='o', color='r')

plt.xlabel('X轴')
plt.ylabel('Y轴')
plt.title('离散值曲线（平滑）')
plt.grid(True)
plt.show()
