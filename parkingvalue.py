import scipy.io as scio  
import matplotlib.pyplot as plt
import numpy as np
from pylab import *
import seaborn as sns
from matplotlib.font_manager import *
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
myfont = FontProperties(fname=r'C:\Windows\Fonts\MSYH.TTC',size=14)
# figure(figsize=(8,6), dpi=300)
plt.subplot(1,1,1)
sns.set_style('darkgrid')
x = np.linspace(0,96,256,endpoint=True)
for i in range(10):
	plt.plot(li[i],linewidth=1.0,linestyle='-',label=lab[i])
plt.legend(loc='lower left')
plt.legend(prop=myfont)
plt.axis([0,100,0,350])
plt.plot([72,72],[0,300], color ='gray', linewidth=2.5, linestyle="-")
plt.plot([76,76],[0,300], color ='gray', linewidth=2.5, linestyle="-")

# plt.figtext(74,300,'figure words',color='green')  
plt.annotate(r'$x_i$~N($μ_i,σ_i^2$)',fontsize=20,xy=(74,300),xytext=(80,320),bbox=dict(boxstyle="round", fc="w"),arrowprops=dict(facecolor='gray', shrink=0.05))
plt.xticks(lis1,fontsize=16)
plt.yticks([0,50,100,150,200,250,300,350],fontsize=16)
plt.xlabel('Time', fontsize=20)
plt.ylabel('Number of Parking Space', fontsize=20)

fig = plt.gcf()
# fig.patch.set_facecolor('ghostwhite')
fig.set_size_inches(15, 8)
fig.savefig('parkingvalue-600.png', dpi=600, bbox_inches='tight')
plt.show()
