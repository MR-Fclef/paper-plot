import scipy.io as scio  
import matplotlib.pyplot as plt
import numpy as np
from pylab import *
import seaborn as sns

suiji = scio.loadmat('suiji.mat')
wnn_suiji_results = scio.loadmat('wnn_suiji_results.mat') 
y_true = scio.loadmat('y_true.mat')

g = suiji['suiji'][0:288,0]
f = wnn_suiji_results['ynn_123'][0:288,0]
y = y_true['true_value'][0:288,0]
# print(y_true['true_value'][0:288,0])

[s1,s2,s3,s4,s5,s6] = [float(0)]*6
print(s1,s2)

for i in range(len(g)):
	s1 = s1 + y[i] * g[i]
	s2 = s2 + g[i] * g[i]
	s3 = s3 + f[i] * g[i]
	s4 = s4 + y[i] * f[i]
	s5 = s5 + f[i] * g[i]
	s6 = s6 + f[i] * f[i]

a = float(s1*s6 - s3*s4)/(s2*s6-s3*s5)
b = float(s1*s5-s2*s4)/(s3*s5-s2*s6)
print(a,b)

pre = [0]*len(g)
for i in range(len(g)):
	pre[i] = a*g[i] + b*f[i]

subplot(1,1,1)
plt.plot(pre)
plt.plot(y)
plt.show()