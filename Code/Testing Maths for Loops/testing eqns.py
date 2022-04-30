import time as ti
import numpy as np

sr = 25000
srt = 1/25000
n = 200
nlist = [] #list of times to do a loop of n calcs

# it seems that 1+1 does not scale linearly. The average time for a loop of 100 is not 10 times larger
# than the average time for a loop of 10. Therefore we can try other maths that might scale

for x in range(100000):
    
    g=ti.time()

    for o in range(n):
        #o**2
        #4*o + 70
        o**2
        #b=ti.time()
        #2*o**3 + 12*o**2 + 10*o
        #7*o**3 + 4*o**2
        #5*o**3 + 25*o**2 + 25*o + 10
        #2*o**4 + 5*o**3 + 14*o**2 + o + 10
        #o**5 + 8*o**3 + 12*o
        #d=ti.time()
        #e= d-b
        

    h=ti.time()
    j = h-g
    nlist.append(j)


narray = np.array(nlist)
print(j)
print("For a Sample Rate of ", sr)
print("This is the time between readings ", srt)
print("n = ", n)
print("Mean time for loop of n calcs", np.mean(narray))
print("SD for a loop of n calcs", np.std(narray))
single = np.mean(narray)/n
print("Mean of a single calc", single)
mln = srt/single
print("number of math loops for desired sample rate", mln)
