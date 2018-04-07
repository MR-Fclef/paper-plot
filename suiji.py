import scipy.io as scio  
import matplotlib.pyplot as plt
import numpy as np
from pylab import *
# import seaborn as sns
import pylab
import scipy.stats as stats
from matplotlib.font_manager import *
dataFile = 'suiji.mat'  
d = scio.loadmat(dataFile)
data = d['y']
# print(data[3,:][0][0])
# test_data = data[0,:][0][0]

plt.subplot(1,1,1)
#sns.set_style('darkgrid')
x = np.linspace(0,96,256,endpoint=True)
myfont = FontProperties(fname=r'C:\Windows\Fonts\MSYH.TTC',size=16)
real = [0.0]*len(data[1,:][0][0])
for i in range(1):
	data[i,:][0][0] = data[i,:][0][0]/350
for i in range(len(data[1,:][0][0])):
	real[i] = float(data[1,:][0][0][i])/350
print(real)
plt.plot(data[0,:][0][0],linewidth=2.0,linestyle='-.',color='blue',label="stochastic probability")
# plt.plot(data[1,:][0][0],linewidth=2.0,linestyle='--',color='green',label="WNN")
# plt.plot(data[2,:][0][0],linewidth=2.0,linestyle=':',color='blue',label="SAW")
plt.plot(real,linewidth=2.0,linestyle='-',color='black',label="true values")
# plt.annotate('a=0.51   b=0.49',fontsize=20,xy=(100,0.8),xytext=(100,0.9))
plt.xticks(fontsize=18)
plt.yticks([0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1],fontsize=18)
plt.xlabel('Time', fontsize=22)
plt.ylabel('Parking Occupancy', fontsize=22)
plt.legend(prop=myfont,loc='upper right')
plt.grid(True)
fig = plt.gcf()
# fig.patch.set_facecolor('ghostwhite')
fig.set_size_inches(15, 8)
fig.savefig('Parking_Occupancyresults300_SAW2_absuiji.png', dpi=300, bbox_inches='tight')
plt.show()