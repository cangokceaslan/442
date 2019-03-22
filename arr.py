import matplotlib.pyplot as plt
import math
import numpy as np
from scipy.stats import linregress
import statistics as st
x=[20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340]
y=[20,40,60,80,100,120,140,160,180]
data2d = [43,23,25,32,46,55,55,72,73,92,73,56,37,54,33,26,16]
data_add =[59,49,58,86,83,111,128,164,146]
a=st.stdev(data_add)

#error=list(np.array(data2d)**(1/2))
#errors=np.round(np.array(error),2)
#print(errors)
#plt.bar(x,data2d,width=15,align="center",color="cyan",yerr=errors)
#plt.show()
#
#error=list(np.array(data_add)**(1/2))
#errors=np.round(np.array(error),2)
#print(errors)
#plt.bar(y,data_add,width=15,align="center",color="violet",yerr=errors)
#plt.show()

#from sin table https://www.grc.nasa.gov/www/k-12/airplane/tablsin.html
sin_val=[0.174,0.342,0.5,0.643,0.766,0.866,0.939,0.984,1.00]
dN=[59,49,58,86,83,111,128,164,146]

errorx=[7.681,7.0,7.615,9.273,9.110,10.535,11.313,12.806,12.083]
xerr=np.array(sin_val)

yarr=np.array(data_add)
errors=np.array(errorx)
slope,intercept,rvalue,pvalue,stderr=linregress(xerr,yarr)
fit=np.polyfit(xerr,yarr,1)
bfl=np.poly1d(fit)
plt.errorbar(xerr,yarr,yerr=errors,linestyle="")
chisquare=np.sum((np.polyval(fit,xerr)-yarr)**2)
plt.scatter(xerr,yarr)
plt.plot(xerr,bfl(xerr),"")
plt.errorbar(xerr,yarr,yerr=errors,color="b",fmt="o")
plt.title("sin(theta/2)vs dN")
plt.xlabel("sin(theta/2)")
plt.ylabel("Number of Counts")
plt.show()
print(slope)
print(stderr)
x = []
y = []
plt.show()
