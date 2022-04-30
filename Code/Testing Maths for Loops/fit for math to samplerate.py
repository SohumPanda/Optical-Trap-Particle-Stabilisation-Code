from ADCDACPi import ADCDACPi
import time as ti
import numpy as np
import matplotlib.pyplot as plt

#DATA FOR READVSR() ONLY ONE CHANNEL

loopno = np.array([5,10,20,30,40,50,60,70,80,90,100,120,140,160,180,200,225,250,275,300,325,350,375,400,425])
samplerate = np.array([27866.21619578718,27643.107524396135,27486.295837111327,27346.97219390276,27065.37797982689,26857.449666764598,26649.67935266733,26577.59626222066,26185.94623061017,25852.053509932583,25746.90890386799,25476.50982110766,25206.754487024176,24671.156504872964,24291.206546132777,24092.03343862163,23542.054865963764,23042.322000080803,22340.607210955935,21753.000207594774,20924.61549891649,20266.377713441245,19617.22564360222,19162.911313208988,
18625.875878985164])

#fit,cov = np.polyfit(loopno,samplerate,1,cov=True)
#fitplot = np.poly1d(fit)
#sig0 = np.sqrt(cov[0,0])
#sig1 = np.sqrt(cov[1,1])

#plt.plot(loopno, fitplot(loopno))
#plt.plot(loopno,samplerate, 'x')
#plt.show()

#print('Slope = %.10f +- %.4f' %(fit[0],sig0))
#print('Intercept = %.10f +- %.4f' %(fit[1],sig1))
#print('Equation')
#print(fitplot)

#we now want an eqn for sample rate to loop number, so we swap the x and y
# this way for a desired sample rate, we can figure out what the loop number should be


#fit_a,cov_a = np.polyfit(samplerate,loopno,1,cov=True)
#fit_aplot = np.poly1d(fit_a)
#sig_a0 = np.sqrt(cov_a[0,0])
#sig_a1 = np.sqrt(cov_a[1,1])

#plt.grid()
#plt.xlabel('Sample Rate (Hz)')
#plt.ylabel('Number of Maths Loops')
#plt.plot(samplerate, fit_aplot(samplerate))
#plt.plot(samplerate,loopno, 'x')
#plt.show()

#print('Slope = %.10f +- %.4f' %(fit_a[0],sig_a0))
#print('Intercept = %.10f +- %.4f' %(fit_a[1],sig_a1))
#print('Equation')
#print(fit_aplot)

#x = fit_aplot(26000)



#DATA FOR READVBOTHSR() 2 CHANNElS SIMULTANEOUSLY

loopno_both = np.array([10,50,100,150,175,200,225,250,275,300,350,400,450])
sr_both = np.array([14441.713033231015,14122.946593423796,13703.730915949325,13479.466313297991,13361.293059211142,13203.322207799438,13086.593461379982,12914.020839160197,12585.246452308525,12384.059147293376,11950.716350326667,11520.38401666065,11241.839908590291])

fit_b,cov_b = np.polyfit(sr_both,loopno_both,1,cov=True)
fit_bplot = np.poly1d(fit_b)
sig_b0 = np.sqrt(cov_b[0,0])
sig_b1 = np.sqrt(cov_b[1,1])

plt.grid()
plt.xlabel('Sample Rate (Hz)')
plt.ylabel('Number of Maths Loops')
plt.plot(sr_both, fit_bplot(sr_both))
plt.plot(sr_both,loopno_both, 'x')
plt.show()

print('Slope = %.10f +- %.4f' %(fit_b[0],sig_b0))
print('Intercept = %.10f +- %.4f' %(fit_b[1],sig_b1))
print('Equation')
print(fit_bplot)
