# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 16:39:49 2022

@author: me
"""
import time as ti
import numpy as np
import matplotlib.pyplot as plt


def exp_weights(window_size):
    # returns weights exp(0) ... exp(1) that are normalised (sum to 1)
    unnormalised_weights = np.exp(np.linspace(0, 1, window_size))
    return unnormalised_weights / np.sum(unnormalised_weights)


def test_data_maker(num_samples, end):
    t = np.linspace(end, end + 2 * np.pi, num_samples)
    v = 2 + np.sin(t) # + np.random.normal(loc=0, scale=1)
    return v, t


def continuous_read_moving_avg(channel, no_samples, input_samplerate, no_runs, window_size = 10):
   #no_runs is how many times we run readv().
    start = ti.time()
    savetimes = []
    starttimes = []
    endtimes = []
    
    moving_avg_window = []
    moving_avg_pairs = []
    moving_avg_weights = exp_weights(window_size)
    end = 0
    
    for n in range(no_runs):
        v,t = test_data_maker(100, end) #readvsr(channel, no_samples, input_samplerate)
        end = t[-1]
        if len(moving_avg_window) == 0:
            moving_avg_window = [(t[i], v[i]) for i in range(window_size)] # first (say) 10 (t,v) pairs
        
        for end_idx in range(window_size, len(v)):
            moving_avg_window.pop(0)
            
            moving_avg_window.append((t[end_idx], v[end_idx]))
            t_avg = np.average([pair[0] for pair in moving_avg_window], weights = moving_avg_weights)
            v_avg = np.average([pair[1] for pair in moving_avg_window], weights = moving_avg_weights)
            
            moving_avg_pairs.append((t_avg, v_avg))
            
        
        data = np.column_stack((t,v))
        a = ti.time()
        np.savetxt('batch'+str(n), data, delimiter=',')
        b = ti.time()
        c = b-a
        savetimes.append(c)
        starttimes.append(start)
        endtimes.append(end)

    for i in range(len(starttimes)):
        starttimes[i]-=start

    for j in range(len(endtimes)):
        endtimes[j]-=start
        
    del starttimes[0] 
    del endtimes[-1]
    
    gapsarray = np.array(starttimes) - np.array(endtimes)
    gaps = gapsarray.tolist()
    
    return savetimes, gaps, moving_avg_pairs


def testy():
    foo, bar, moving_avg_pairs = continuous_read_moving_avg(None, None, None, 100)
    times = np.array([pair[0] for pair in moving_avg_pairs])
    for tee in times:
        if 6 < tee and tee < 8:
            print(f"found t = {tee:.3f}")
    v_avgs = np.array([pair[1] for pair in moving_avg_pairs])
    
    plt.grid()
    plt.xlim(5, 5 + 2 * np.pi)
    plt.plot(times, v_avgs, 'bx')
    plt.plot(times, np.sin(times), 'rx')
    
testy()