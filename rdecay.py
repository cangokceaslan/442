import matplotlib.pyplot as plt
import math
import numpy as np
from scipy.stats import linregress
import statistics as st

lns=[2.596746132,2.886475288,3.132446097,3.476614021]
val_t=[11.33,27.005,47.435,75.075]
t5t2500=np.array([17.01,30.89,48.085,70.265])
t5t3000=np.array([11.33,27.005,47.435,75.075])
t5t3500=np.array([10,25.595,44.49,69.275])
t5t4000=np.array([26.56,56.805,86.905,136.595])
t5t4500=np.array([10.93,27.69,63.345,114.805])

t10t2500=np.array([15.765,37.59,66.88,114.585])
t10t3000=np.array([18.475,42.06,74.92,131.72])
t10t3500=np.array([18.06,35.69,57.94,88.7] )
t10t4000=np.array([10.395,26.135,45.135,70.215])
t10t4500=np.array([6.63,17.27,31.06,49.31] )

t15t2500=np.array([9.81,24.91,43.275,66.61 ])
t15t3000=np.array([9.44,25.54,45.215,71.17 ])
t15t3500=np.array([9.855,28.995,53.55,88.725 ]) 
t15t4000=np.array([24.97,46.95,77.44,127.805 ])
t15t4500=np.array([17.825,40.28,71.565,125.295 ]) 

s5s2500=np.log(np.array([12.62,15.14,19.25,25.11]))
s5s3000=np.log(np.array([13.42,17.93,22.93,32.35 ]))
s5s3500=np.log(np.array([14.42,16.77,21.02,28.55 ]))
s5s4000=np.log(np.array([35.1,25.39,34.81,64.57 ]))
s5s4500=np.log(np.array([15.44,18.08,53.23,49.69 ]))

s10s2500=np.log(np.array([20.29,23.36,35.22,60.19 ]))
s10s3000=np.log(np.array([20.49,26.68,39.04,74.56 ]))
s10s3500=np.log(np.array([15.84,19.42,25.08,36.44 ] ))
s10s4000=np.log(np.array([14.31,17.17,20.83,29.33 ]))
s10s4500=np.log(np.array([9.26,12.02,15.56,20.94 ] ))

s15s2500=np.log(np.array( [13.78,16.42,20.31,26.36  ]))
s15s3000=np.log(np.array([14.76,17.44,21.9,30]))
s15s3500=np.log(np.array( [17.27,21.01,28.1,42.25  ] ))
s15s4000=np.log(np.array( [19.34,24.62,36.36,64.37]))
s15s4500=np.log(np.array( [19.43,25.48,37.09,70.37 ] ))

xarr = np.array(val_t)
yarr=np.array(lns)
slope,intercept,rvalue,pvalue,stderr=linregress(xarr,yarr)
slope_array,std_array =[],[]
slope,intercept,rvalue,pvalue,stderr=linregress(t5t2500,s5s2500)
slope_array.append(slope);std_array.append(stderr)
slope,intercept,rvalue,pvalue,stderr=linregress(t5t3000,s5s3000)
slope_array.append(slope);std_array.append(stderr)
slope,intercept,rvalue,pvalue,stderr=linregress(t5t3500,s5s3500)
slope_array.append(slope);std_array.append(stderr)
slope,intercept,rvalue,pvalue,stderr=linregress(t5t4000,s5s4000)
slope_array.append(slope);std_array.append(stderr)
slope,intercept,rvalue,pvalue,stderr=linregress(t5t4500,s5s4500)
slope_array.append(slope);std_array.append(stderr)
slope,intercept,rvalue,pvalue,stderr=linregress(t10t2500,s10s2500)
slope_array.append(slope);std_array.append(stderr)
slope,intercept,rvalue,pvalue,stderr=linregress(t10t3000,s10s3000)
slope_array.append(slope);std_array.append(stderr)
slope,intercept,rvalue,pvalue,stderr=linregress(t10t3500,s10s3500)
slope_array.append(slope);std_array.append(stderr)
slope,intercept,rvalue,pvalue,stderr=linregress(t10t4000,s10s4000)
slope_array.append(slope);std_array.append(stderr)
slope,intercept,rvalue,pvalue,stderr=linregress(t10t4500,s10s4500)
slope_array.append(slope);std_array.append(stderr)
slope,intercept,rvalue,pvalue,stderr=linregress(t15t2500,s15s2500)
slope_array.append(slope);std_array.append(stderr)
slope,intercept,rvalue,pvalue,stderr=linregress(t15t3000,s15s3000)
slope_array.append(slope);std_array.append(stderr)
slope,intercept,rvalue,pvalue,stderr=linregress(t15t3500,s15s3500)
slope_array.append(slope);std_array.append(stderr)
slope,intercept,rvalue,pvalue,stderr=linregress(t15t4000,s15s4000)
slope_array.append(slope);std_array.append(stderr)
slope,intercept,rvalue,pvalue,stderr=linregress(t15t4500,s15s4500)
slope_array.append(slope);std_array.append(stderr)
total,wtotal = 0,0
for x in range(15):
    w = (1/(std_array[x])**2)
    total += slope_array[x] * w
    wtotal += w
lamb = total / wtotal
sigma = np.sqrt(1/wtotal)
print(sigma)
hlife=math.log(2)/lamb
print(hlife)
sigmahlife = ((np.log(2)/(lamb**2))) * (sigma)
print(sigmahlife)
fit=np.polyfit(xarr,yarr,1)
bfl=np.poly1d(fit)
plt.scatter(xarr,yarr)
plt.plot(xarr,bfl(xarr),"")
plt.title("sin(theta/2)vs dN")
plt.xlabel("sin(theta/2)")
plt.ylabel("Number of Counts")
plt.show()

x = []
y = []
plt.show()