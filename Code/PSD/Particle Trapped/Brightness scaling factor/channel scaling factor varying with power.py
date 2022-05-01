import numpy as np
import matplotlib.pyplot as plt

# OLD DATA 
# powers = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9] #want this as x as we will be measuring this from now
# factors = [1.02943288, 1.03148926, 1.03266338, 1.0316673, 1.03320726, 1.0352925, 1.03274136, 1.03377324, 1.0377772, 1.03576018] #want this as y as this is what we will be calculating
# 
# p_err = [0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05]
# top_err = [1,1,2,1,3,1,1,1,2]

# DATA FROM STABLE PARTICLE Z

powers = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.1,1.2,1.3,1.4,1.5] #want this as x as we will be measuring this from now
factors = [1.0296271,1.0298594,1.0304939,1.0320702,1.0335317,1.0366192,1.0378429,1.0451071,1.055113,1.0657845,1.0758468,1.0995903,1.1086663,1.1306254,1.1401196,1.1640253] #want this as y as this is what we will be calculating

p_err = [0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05]
top_err = [1,1,2,1,3,1,1,1,2]

#fit,cov = np.polyfit(back,top,1, w = 1/np.array(top_err), cov=True)



fit,cov = np.polyfit(powers,factors,2, cov=True)
fitplot = np.poly1d(fit)
sig0 = np.sqrt(cov[0,0])
sig1 = np.sqrt(cov[1,1])

plt.plot(powers, fitplot(powers))
#plt.plot(back,top, 'x',)
#plt.errorbar( back, top, yerr = top_err, xerr=back_err, fmt='x')
plt.errorbar(powers, factors, xerr = p_err, fmt='x', markersize = 15)
plt.title('Channel Scaling Factor vs Incident Laser Power', fontsize = 40)
plt.ylabel('Channel Scaling Factor', fontsize = 30)
plt.xlabel('Incident Laser Power (\u03BCW)', fontsize = 30)
plt.ylabel('Channel Scaling Factor', fontsize = 30)
plt.xticks(fontsize = 30)
plt.yticks(fontsize = 30)
#plt.legend(loc='best', fontsize = 20)
plt.grid()
plt.show()

print('Slope = %.10f +- %.4f' %(fit[0],sig0))
print('Intercept = %.10f +- %.4f' %(fit[1],sig1))
print('Equation')
print(fitplot)
