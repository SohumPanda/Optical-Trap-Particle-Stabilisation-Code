# Optical-Trap-Particle-Stabilisation-Code
Python code to use for Pi 4 with ADCDAC Pi 0 board for real time trapped particle stabilisation 

In the Code folder is the sampling code and code to plot the data saved from sampling the particle's motion. All data saved from sampling particle motion are in Code/PSD/Particle Trapped. We were able to develop and test the real time feedback code for one particle, particle ac, and the data from that run is withtin Code/PSD/Particle Trapped/Feedback.

The Code folder contains data on: Finding the fastest clock speed for the ADC to talk to the Pi 4, Fourier Transforms of the AC components of the laser power at a range of different powers, Analysis of the laser power swing produced by the Pockels Cell at different polariser angles, analysis of the statistical noise from reading data and how physical location of the Pi changes noise (PSD folder).  

In the Trapped Particle folder are pictures of the fringes produced by each particle when trapped and the graphs for the fringe spacings produced by the analysis of the fringe pictures in ImageJ. In this folder is also the code to calculate the sizes of the particles from their fringe spacing and compare it to the sizes of the particles observed directly from the CCD camera 
