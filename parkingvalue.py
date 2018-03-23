import scipy.io as scio  
import matplotlib.pyplot as plt
import numpy as np
from pylab import *
import seaborn as sns
dataFile = 'parkingvalue.mat'  
d = scio.loadmat(dataFile)  
# print type(data) 
data = d['data2']
day1 = data[0,0][0]
day2 = data[1,0][0]
day3 = data[2,0][0]
day4 = data[3,0][0]
day5 = data[4,0][0]
day6 = data[5,0][0]
day7 = data[6,0][0]
day8 = data[7,0][0]
day9 = data[8,0][0]
day10 = data[9,0][0]
li = []
lab = []
for i in range(10):
	li.append(data[i,0][0])
	lab.append("day"+str(i+1))
print(lab)
# print(day1)
# print(day2)
# print(day3)
# print(day4)
# print(day5)
# print(day6)
# print(day7)
# print(day8)
# print(day9)
# print(day10)
lis1 = [int(i) for i in range(0,97,8)]
print(lis1)

# figure(figsize=(8,6), dpi=300)
subplot(1,1,1)
sns.set_style('darkgrid')
x = np.linspace(0,96,256,endpoint=True)
for i in range(10):
	plot(li[i],linewidth=1.0,linestyle='-',label=lab[i])
legend(loc='lower left')
plt.axis([0,100,0,350])
plot([72,72],[0,300], color ='gray', linewidth=2.5, linestyle="-")
plot([76,76],[0,300], color ='gray', linewidth=2.5, linestyle="-")

plt.figtext(74,300,'figure words',color='green')  
plt.annotate('x_i~N(μ_i,σ_i^2)',xy=(74,300),xytext=(80,320),bbox=dict(boxstyle="round", fc="w"),arrowprops=dict(facecolor='gray', shrink=0.05))

# 设置轴记号
xticks(lis1)
yticks([0,50,100,150,200,250,300,350])
# xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
#        [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])

# yticks([-1, 0, +1],
#        [r'$-1$', r'$0$', r'$+1$'])
# 在屏幕上显示
show()

# figure(figsize=(8,6), dpi=80)

# # 创建一个新的 1 * 1 的子图，接下来的图样绘制在其中的第 1 块（也是唯一的一块）
# subplot(1,1,1)

# X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
# C,S = np.cos(X), np.sin(X)
# # 绘制余弦曲线，使用蓝色的、连续的、宽度为 1 （像素）的线条
# plot(X, C, color="blue", linewidth=1.0, linestyle="-")

# # 绘制正弦曲线，使用绿色的、连续的、宽度为 1 （像素）的线条
# plot(X, S, color="r", lw=4.0, linestyle="-")

# plt.axis([-4,4,-1.2,1.2])
# # 设置轴记号

# xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
#        [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])

# yticks([-1, 0, +1],
#        [r'$-1$', r'$0$', r'$+1$'])
# # 在屏幕上显示
# show()