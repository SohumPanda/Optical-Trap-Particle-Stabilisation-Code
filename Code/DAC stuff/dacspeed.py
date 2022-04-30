from ADCDACPi import ADCDACPi
import time as ti
import numpy as np

#import matplotlib.pyplot as plt
# create an instance of the ADCDAC Pi with a DAC gain set to 1 or 2 depending on if
# you want 0 to 2.048 or 3.3 V 
adcdac = ADCDACPi(2)

# set the reference voltage.  this should be set to the exact voltage
# measured on the raspberry pi 3.3V rail.
adcdac.set_adc_refvoltage(3.3)



def dacrate(no_samples):

    start = ti.time()
    counter = 1
    
    while counter<= no_samples:
        adcdac.set_dac_raw(1, 4095)  # set the voltage on channel 1 to 3.3V
        counter = counter + 1
        
    end = ti.time()
    totalt = end - start 
    print(totalt)
    setrate = (no_samples)/totalt
    print(setrate)

        
def dacrate_withadc(no_samples):
        
    start = ti.time()
    counter = 1    
        
    while counter<= no_samples:
        adcdac.read_adc_voltage(1, 0)
        adcdac.set_dac_raw(1, 4095)  # set the voltage on channel 1 to 3.3V
        counter = counter + 1
        
    end = ti.time()
    totalt = end - start 
    print(totalt)
    setrate = (no_samples)/totalt
    print(setrate)
    
def dacrate_withadcboth(no_samples):
        
    start = ti.time()
    counter = 1    
        
    while counter<= no_samples:
        adcdac.read_adc_voltage(1, 0)
        adcdac.read_adc_voltage(2, 0)
        adcdac.set_dac_raw(1, 4095)  # set the voltage on channel 1 to 3.3V
        counter = counter + 1
        
    end = ti.time()
    totalt = end - start 
    print(totalt)
    setrate = (no_samples)/totalt
    print(setrate)

dacrate_withadcboth(100000)