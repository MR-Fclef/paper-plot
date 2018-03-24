import scipy.io as scio  
import matplotlib.pyplot as plt
import numpy as np
from pylab import *
import seaborn as sns
import pylab
import scipy.stats as stats

dataFile = 'norm_plot1.mat'  
d = scio.loadmat(dataFile)
data = d['xc']
test_data = data[0,:][0][0]

# measurements = np.random.normal(loc = 20, scale = 5, size=100)  
# print(measurements)
stats.probplot(test_data, dist="norm", plot=pylab)
plt.title('Probability Plot',fontsize=20)
plt.xlabel('Theoretical quantiles', fontsize=20)
plt.ylabel('Ordered Values', fontsize=20)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
fig = plt.gcf()
# fig.patch.set_facecolor('ghostwhite')
fig.set_size_inches(15, 8)
fig.savefig('norm_test300.tiff', dpi=300, bbox_inches='tight')
pylab.show()