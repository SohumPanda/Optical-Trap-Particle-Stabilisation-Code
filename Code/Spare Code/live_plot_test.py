import matplotlib.pyplot as plt
from random import random
from ADCDACPi import ADCDACPi
import time as ti
import numpy as np

# create an instance of the ADCDAC Pi with a DAC gain set to 1 for 0 - 2.048 V, 2 for 0 - 3.3 V
adcdac = ADCDACPi(2)

# set the reference voltage.  this should be set to the exact voltage
# measured on the raspberry pi 3.3V rail.
adcdac.set_adc_refvoltage(3.3)

plt.ion()

v=[0]*10
t=list(range(0,10))

a=plt.subplot()
l, = a.plot(t,v)
plt.ylim((0,2))

while True:
    v.append(adcdac.read_adc_voltage(1, 0))
    v.remove(v[0])
    l.set_ydata(v)
    print(v)
    plt.pause(1.0001)