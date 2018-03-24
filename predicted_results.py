import scipy.io as scio  
import matplotlib.pyplot as plt
import numpy as np
from pylab import *
import seaborn as sns
import pylab
import scipy.stats as stats
from matplotlib.font_manager import *
dataFile = 'predicted_results.mat'  
d = scio.loadmat(dataFile)
data = d['yyc']
print(data[0,:][0][0])
# test_data = data[0,:][0][0]

plt.subplot(1,1,1)
sns.set_style('darkgrid')
x = np.linspace(0,96,256,endpoint=True)
myfont = FontProperties(fname=r'C:\Windows\Fonts\MSYH.TTC',size=16)
plt.plot(data[0,:][0][0],linewidth=1.0,linestyle='-.',color='red',label="Lyapunov")
plt.plot(data[1,:][0][0],linewidth=1.0,linestyle='--',color='green',label="WNN")
plt.plot(data[2,:][0][0],linewidth=1.0,linestyle=':',color='blue',label="SAW")
plt.plot(data[3,:][0][0],linewidth=1.0,linestyle='-',color='black',label="true values")
plt.xticks(fontsize=16)
plt.yticks([0,50,100,150,200,250,300,350],fontsize=16)
plt.xlabel('Time', fontsize=20)
plt.ylabel('Number of Parking Space', fontsize=20)
plt.legend(prop=myfont,loc='upper right')
fig = plt.gcf()
# fig.patch.set_facecolor('ghostwhite')
fig.set_size_inches(15, 8)
fig.savefig('predicted_results300.tiff', dpi=300, bbox_inches='tight')
plt.show()
