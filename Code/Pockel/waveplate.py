import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as spo

angle = [0,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,85,95,125,135]
ang_err = 23*[2]
power = [112.6,35.3,3.54,46.8,155.2,233.2,297.1,277.4,200.6,100.3,29.80,7.97,52.2,156.2,258.1,311.5,296.6,220.9,113.6,145.1,56.1,99.4,200.4]         
p_err = [1,2,0.2,0.02,2,3,3,2,1,0.6,0.8,0.02,0.5,0.9,2,3,3,2,1,0.3,0.4,0.5,0.9]

xx = np.arange(0,180,1)

### At certain angles, plot what the power changes to fro changing the voltage across the pockel cell

## 60 Degrees ##

pcell_voltage60 = [0,-50,-100,-150,-192,50,100,150,192]
angle60 = 9*[60]
power60 = [297.1,302.7,307.2,310.4,315.3, 289.1,275.4,264.5,253.6]
p60_err = [2,1,2,3,1,2,2,2,1]


## 70 Degrees ##

pcell_voltage70 = [0,-50,-100,-150,-192,50,100,150,192]
angle70 = 9*[70]
power70 = [277.4,286.3,292.3,295.8,297.1,266.7,253.0,240.1,226.8]
p70_err = [1,1,1,1,1,0.7,1,1,1]


## 80 Degrees ##

pcell_voltage80 = [0,-50,-100,-150,-192,50,100,150,192]
angle80 = 9*[80]
power80 = [200.6,207.3,212.5,215.6,219.8,195.0,187.7,180.2,171.6]
p80_err = [0.8,0.9,0.8,0.8,0.8,0.9,0.7,0.7,0.8]


## 85 Degrees ##

pcell_voltage85 = [0,-50,-100,-150,-192,50,100,150,192]
angle85 = 9*[85]
power85 = [145.1,149.3,152.7,155.5,158.3,137.1,131.2,124.7,119.3]
p85_err = [0.3,0.9,0.7,0.6,0.5,1,0.8,0.6,0.3]


##  90 Degrees ##

pcell_voltage90 = [0,-50,-100,-150,-192,50,100,150,192]
angle90 = 9*[90]
power90 = [100.3,103.6,106.8,109.3,111.3,94.1,89.7,84.0,80.0]
p90_err = [0.4,0.5,0.4,0.8,0.8,0.8,0.5,0.8,0.6]


##  95 Degrees ##

pcell_voltage95 = [0,-50,-100,-150,-192,50,100,150,192]
angle95 = 9*[95]
power95 = [56.1,58.3,60.6,62.6,64.0,52.1,49.1,46.5,43.3]
p95_err = [0.4,0.5,0.5,0.7,0.9,1,0.5,0.7,0.7]

##  100 Degrees ##

pcell_voltage100 = [0,-50,-100,-150,-192,50,100,150,192]
angle100 = 9*[100]
power100 = [29.80,31.6,33.3,34.65,35.9,27.3,25.4,23.4,21.8]
p100_err = [0.2,0.2,0.3,0.2,0.3,0.3,0.2,0.3,0.3]


##  110 Degrees ##

pcell_voltage110 = [0,-50,-100,-150,-192,50,100,150,192]
angle110 = 9*[110]
power110 = [7.97,7.21,6.51,5.75,5.20,7.88,8.31,9.09,8.73]
p110_err = [0.07,0.07,0.09,0.06,0.06,0.09,0.1,0.1,0.1]


##  120 Degrees ##

pcell_voltage120 = [0,-50,-100,-150,-192,50,100,150,192]
angle120 = 9*[120]
power120 = [52.2,50.3,47.3,43.8,40.9,54.8,56.0,56.7,57.0]
p120_err = [0.9,0.3,0.5,0.8,0.4,0.6,0.3,0.2,0.3]


##  125 Degrees ##

pcell_voltage125 = [0,-50,-100,-150,-192,50,100,150,192]
angle125 = 9*[125]
power125 = [99.4,97.3,94.9,92.4,89.7,101.1,102.1,102.6,103.5]
p125_err = [0.5,0.7,0.5,0.3,0.6,0.4,0.5,0.5,0.8]


##  130 Degrees ##

pcell_voltage130 = [0,-50,-100,-150,-192,50,100,150,192]
angle130 = 9*[130]
power130 = [156.2,154.4,151.3,146.8,143.1,157.4,158.4,158.5,158.7]
p130_err = [0.9,1,0.7,0.8,0.7,0.6,0.9,0.6,0.6]


##  135 Degrees ##

pcell_voltage135 = [0,-50,-100,-150,-192,50,100,150,192]
angle135 = 9*[135]
power135 = [200.4,198.5,195.1,190,184.3,201.8,201.7,200.9,199.6]
p135_err = [0.9,1,0.5,0.6,0.5,0.6,0.8,0.4,1]


##  140 Degrees ##

pcell_voltage140 = [0,-50,-100,-150,-192,50,100,150,192]
angle140 = 9*[140]
power140 = [258.1,251.2,247.6,240.9,234.8,260,260.2,258.2,259.7]
p140_err = [1,2,1,1,1,1,2,1,0.9]





def cossquared(x,a,b,c,d):  #a is 2x, 3x etc  #b is phase shift   #c scale factor   #d is y shift 
    cssq = (np.cos((a*x*2*np.pi/360) + (b*np.pi/180)))**2
    return (c*cssq)+d

p=[2, -120, 315, 5] #a is 2x, 3x etc  #b is phase shift   #c scale factor   #d is y shift 
fit,cov=spo.curve_fit(cossquared, angle, power, p)
print(*fit)
plt.plot(xx, cossquared(xx, *fit), color='red', linewidth = 2)



#plt.plot(angle,power, 'bx')
plt.title('Delivered Laser Power against Polariser Angle', fontsize = 40)
plt.errorbar(angle, power, xerr = ang_err, yerr=p_err, fmt='x', color='red', markersize = 15)
plt.errorbar(angle60[1:], power60[1:], yerr=p60_err[1:], fmt = 'x', color = 'blue', markersize = 15)
plt.errorbar(angle70[1:], power70[1:], yerr=p70_err[1:], fmt = 'x', color = 'blue', markersize = 15)
plt.errorbar(angle80[1:], power80[1:], yerr=p80_err[1:], fmt = 'x', color = 'blue', markersize = 15)
plt.errorbar(angle85[1:], power85[1:], yerr=p85_err[1:], fmt = 'x', color = 'blue', markersize = 15)
plt.errorbar(angle90[1:], power90[1:], yerr=p90_err[1:], fmt = 'x', color = 'blue', markersize = 15)
plt.errorbar(angle95[1:], power95[1:], yerr=p95_err[1:], fmt = 'x', color = 'blue', markersize = 15)
plt.errorbar(angle100[1:], power100[1:], yerr=p100_err[1:], fmt = 'x', color = 'blue', markersize = 15)
plt.errorbar(angle110[1:], power110[1:], yerr=p110_err[1:], fmt = 'x', color = 'blue', markersize = 15)
plt.errorbar(angle120[1:], power120[1:], yerr=p120_err[1:], fmt = 'x', color = 'blue', markersize = 15)
plt.errorbar(angle125[1:], power125[1:], yerr=p125_err[1:], fmt = 'x', color = 'blue', markersize = 15)
plt.errorbar(angle130[1:], power130[1:], yerr=p130_err[1:], fmt = 'x', color = 'blue', markersize = 15)
plt.errorbar(angle135[1:], power135[1:], yerr=p135_err[1:], fmt = 'x', color = 'blue', markersize = 15)
plt.errorbar(angle140[1:], power140[1:], yerr=p140_err[1:], fmt = 'x', color = 'blue', markersize = 15)

plt.grid()
plt.xlabel('Angle (Degrees)', fontsize = 30)
plt.ylabel('Laser Power (mW)', fontsize = 30)
plt.xticks(fontsize = 30)
plt.yticks(fontsize = 30)
plt.show()

