from ADCDACPi import ADCDACPi
import time as ti
import numpy as np
import matplotlib.pyplot as plt

# create an instance of the ADCDAC Pi with a
#DAC gain set to 1 for a voltage range of 0 - 2.048 V, 2 for a voltage range of 0 - 3.3 V
adcdac = ADCDACPi(2)

#by using gain 2, we can set the DAC output voltage to be up to 3.3V, which is the max we can read from the ADC


# set the reference voltage.  this should be set to the exact voltage
# measured on the raspberry pi 3.3V rail.
adcdac.set_adc_refvoltage(3.3)


# using this function, we can set the voltage output to a channel.
# set_dac_voltage(channel, voltage)
adcdac.set_dac_voltage(1, 3.1)
adcdac.set_dac_voltage(1, 0)

#while True:
    #adcdac.set_dac_voltage(1, 0)
    #adcdac.set_dac_raw(1, 4095)
    
#Square Wave Func
    
# while True:
#     adcdac.set_dac_voltage(1, 2)  # set the voltage on channel 1 to 1.5V
#     ti.sleep(2)  # wait 0.5 seconds
#     adcdac.set_dac_voltage(1, 0)  # set the voltage on channel 1 to 0V
#     ti.sleep(2)  # wait 0.5 seconds

    