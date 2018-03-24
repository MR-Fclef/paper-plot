import scipy.io as scio  
import matplotlib.pyplot as plt
import numpy as np
from pylab import *
import seaborn as sns
import pylab
import scipy.stats as stats
from matplotlib.font_manager import *
dataFile = 'compute_time.mat'  
d = scio.loadmat(dataFile)
data = d['compute_time']
print(data)
test_data = data[0,:][0][0]
print(test_data)

for i in range(len(test_data)):
	test_data[i] = test_data[1]

plt.subplot(1,1,1)
# sns.set_style('darkgrid')
x = np.linspace(0,96,256,endpoint=True)
myfont = FontProperties(fname=r'C:\Windows\Fonts\MSYH.TTC',size=16)
plt.plot([int(i) for i in range(0,300,3)],test_data,linewidth=1.0,linestyle=':',color='blue',label="SAW")
plt.plot([int(i) for i in range(0,300,3)],data[1,:][0][0],linewidth=1.0,linestyle='--',color='green',label="WNN")
plt.plot([int(i) for i in range(0,300,3)],data[2,:][0][0],linewidth=1.0,linestyle='-.',color='red',label="Lyapunov")
plt.xticks([int(i) for i in range(0,300,30)],fontsize=16)
plt.yticks(fontsize=16)
plt.xlabel('Number of Steps', fontsize=20)
plt.ylabel('Computional Time', fontsize=20)
plt.legend(prop=myfont,loc='upper left')
fig = plt.gcf()
# fig.patch.set_facecolor('ghostwhite')
fig.set_size_inches(15, 8)
fig.savefig('compute_time_300.tiff', dpi=300, bbox_inches='tight')
plt.show()



