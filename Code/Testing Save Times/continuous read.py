def continuous_read(channel, batch_size):
    n = 1
    while True:
        t,v = readv(channel, batch_size)
        data = np.column_stack((t,v))
        np.savetxt('batch'+str(n), data, delimiter=',')
        n+=1
    return
               