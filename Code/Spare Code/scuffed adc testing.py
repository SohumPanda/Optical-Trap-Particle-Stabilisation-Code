from ADCDACPi import ADCDACPi
import numpy as np
import matplotlib.pyplot as plt
import time
import matplotlib

#hashtag is shift + 3 on my bluetooth keyboard 
#we expect to measure a signal 1/3 of what we feed in due to the circuit
#on the ADCDAC dividing the voltaage by 3 

adcdac = ADCDACPi(2)
#gain factor = 1 sets ADC V range 0 - 2.048 V
#gain factor = 2 sets ADC V range 0 - 3.3   V

adcdac.set_adc_refvoltage(3.3)
#The ADC uses the raspberry pi 3.3V power as a voltage reference

print (adcdac.read_adc_voltage(1,0))
#channel 1 = signal on ADCDAC going into in 1
#channel 2 = signal on ADCDAC going into in 2
#if you change the channel to thee one with no signal in the voltage measured is 0, which makes sense. 

voltage = []
count=100000
starttime=time.perf_counter()
while count>0:
    voltage.append(adcdac.read_adc_voltage(1,0))
    count=count-1
    
endtime=time.perf_counter()
elapsed=endtime - starttime
time=np.linspace(0,elapsed,100)
varray=np.array(voltage)
print(elapsed)
print(time)

plt.figure('test')
plt.grid()
plt.plot(time,varray)
plt.savefig("test1.png")   
plt.show



