import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial.polynomial import Polynomial

# 分段点之后的数据 (x > 0.98)
# x2 = np.array([0.98, 0.985, 0.99, 0.992, 0.994, 0.996, 0.998, 1.0])
# y2 = np.array([0.9505, 0.8980, 0.8890, 0.7965, 0.7475, 0.6255, 0.5205, 0.5025])

x2 = np.array([0.975, 0.98, 0.985, 0.987, 0.99, 0.992, 0.994, 0.998, 1.0])
y2 = np.array([ 0.8256, 0.7940, 0.7532, 0.7359, 0.7010, 0.6065, 0.5770, 0.5243, 0.5030])

# 使用五次多项式拟合
poly5 = Polynomial.fit(x2, y2, 5)

# 生成平滑数据进行绘图
x2_smooth = np.linspace(x2.min(), x2.max(), 500)
y2_smooth = poly5(x2_smooth)

# 计算曲率
y2_deriv = np.gradient(y2_smooth, x2_smooth)
y2_deriv2 = np.gradient(y2_deriv, x2_smooth)
curvature = y2_deriv2 / (1 + y2_deriv**2)**1.5

# 限制x2_smooth和curvature到x<0.998
mask = x2_smooth < 0.998
x2_limited = x2_smooth[mask]
curvature_limited = curvature[mask]

# 绘制更新后的曲线和曲率图像
plt.figure(figsize=(12, 6))


plt.plot(x2_limited, curvature_limited,  color='g')
plt.xlabel('Concentration')
plt.ylabel('Curvature')
plt.title(' ')


plt.legend()
plt.tight_layout()
plt.show()
