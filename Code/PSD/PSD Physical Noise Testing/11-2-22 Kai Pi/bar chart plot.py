#from ADCDACPi import ADCDACPi
import time as ti
import numpy as np
import matplotlib.pyplot as plt

# Start condition, No Foil, Direct Plug Above, No Foil, Frontside of Table # #CONDITION A

#Direct Plug Above (ONLY CAN REACH FRONTSIDE)

#Channel 1 
SD1A = [[0.0003865750074791051], [0.0003753668338162993], [0.00037834036653828975], [0.00038406837274646702], [0.0003886685075702087]]
Mean_SD1A = 0.00038260381763007396
error1A = 5.0049312584459024e-06


#Channel 2 
SD2A = [[0.00048990334482723885], [0.0004847451477272429], [0.0004844364739716276], [0.0004915176596014506], [0.0004919574336012811]]
Mean_SD2A = 0.0004885120119457682
error2A = 3.2753604754565784e-06



# Best Power Supply, No Foil# #CONDITION B

#White Extension Cable (frontside of Table)

#Channel 1 
SD1B = [[0.0003641986827421079], [0.00037600101916065477], [0.00036311678497916383], [0.00036265915262186873], [0.0003712995737877276]]
Mean_SD1B = 0.00036745504265830453
error1B = 5.296018406687141e-06

#Channel 2 
SD2B = [[0.0004656399717306346], [0.00047327149558893], [0.00046637574444502875], [0.00046530301440053925], [0.0004695469997790343]]
Mean_SD2B = 0.0004680274451888334
error2B = 3.0219125974206354e-06



# Best Power, Best Location, No Foil # #CONDITION C

#On top of Enclosure 1 (Big Black Box on Which Monitor is on)

#Channel 1
SD1C = [[0.00016261923112995757], [0.00018117642102150536], [0.00015451938973411196], [0.00016293976643466684], [0.00019587368539744033]]
Mean_SD1C = 0.0001714256987435364
error1C = 0.00001502111074237468

#Channel 2 
SD2C = [[0.00015304672073743127], [0.00016956170481433822], [0.00013872906056407585], [0.00015314338108929223], [0.00018280155985517755]]
Mean_SD2C = 0.00015945648541206302 
error2C = 0.000015216270700312733



# Best Power, Best Location, Foil # #CONDITION D

#Foil

#Channel 1
SD1D = [[0.0001001729557666765], [0.0001522502393233257], [0.00014815474712592124], [0.00011757672456240535], [0.00012424707478831364]]
Mean_SD1D = 0.00012848034831332848
error1D = 0.00001944329074870626


#Channel 2
SD2D = [[0.0000825085752778581], [0.00013389273043985903], [0.00012882449831739561], [0.00010002499181057563], [0.00010766500840745108]]
Mean_SD2D = 0.00011058316085062788
error2D = 0.000018890502001029107

conditions = ['Start','Power Supply','Power Supply & Location','Power Supply, Location & Foil']
data1 = [Mean_SD1A,Mean_SD1B,Mean_SD1C,Mean_SD1D]
data2 = [Mean_SD2A,Mean_SD2B,Mean_SD2C,Mean_SD2D]

errs1 = [error1A,error1B,error1C,error1D]
errs2 = [error2A,error2B,error2C,error2D]

#plt.grid()
width = 0.3
plt.xticks(np.arange(len(data1))+ (width/2), conditions, size=17)
plt.yticks(size=17)
plt.bar(np.arange(len(data1)), data1, yerr = errs1, width = 0.3, label = 'Channel 1')
plt.bar(np.arange(len(data2))+ width, data2, yerr = errs2, width = 0.3, label = 'Channel 2')
#plt.errorbar(a,b, yerr=errs, fmt="None")
plt.ylabel('Average RMS Error for 100,000 points (V)', fontsize = 30)
plt.xlabel('Different Physical Conditions', fontsize = 30)
plt.legend(loc='best', fontsize = 20)
plt.show()

