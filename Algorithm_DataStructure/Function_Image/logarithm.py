# -*- coding: utf-8 -*-
# Product Name: PyCharm
# Project Name: Algorithm_DataStructure
# File Name: logarithm.py
# Date: 2022/06/03 16:53:27
# Author: wangyuankun
# Function: This file is to achieve logarithm function.
import numpy as np
import math
import matplotlib.pyplot as plt

x = np.arange(0.01, 20, 0.02) + 0.01
y1 = [math.log(a, 2) for a in x]
plot1 = plt.plot(x, y1, '-b', label="log2(x)")

# 设置纵坐标范围
plt.ylim(-10, 10)

# 设置横坐标范围
plt.xlim(-0.01, 20)

plt.legend(loc='lower right')

# 保存
plt.savefig("logarithm.png", dpi=None)
plt.show()
