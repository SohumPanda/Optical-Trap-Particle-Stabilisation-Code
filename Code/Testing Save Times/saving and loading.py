import time as ti
import numpy as np
import pandas as pd
#import pyarrow.parquet as pq
#import pyarrow as pa 

t1 = np.array([1,2,3,44,55])
t2 = np.array([12,13,14,15,16])
v1 = np.array([2,3,4,3,2])
v2 = np.array([-2,-1,0,1,2])
data = np.column_stack((t1,t2,v1,v2)) 
print(data)                            # can see how the 4 data columns have been stacked into a 2D array  
print('hello')
a = ti.time()


# SAVING BY USING FEATHER FORMAT TO SAVE AS RAW BINARY
# IF NOT WORKING TRY SAVING USING PICKLE

# convert stacked data in a 2D array to a dataframe in pandas
#df means dataframe 
df = pd.DataFrame(data)
print(data) 
#table = pa.Table.from_pandas(df)
#pq.write_table(table, 'example.parquet')
#pd.DataFrame.to_feather('featherfile.feather')

#save dataframe to pickle file
df.to_pickle('pickle.pkl')



#SAVING WITH np.save() 

#np.save('save',data)

#SAVING WITH np.savetxt()

# Testing Saving to external SSD
# for some reason when i put a file there and copy the path it looks like this but this works 
#np.savetxt('/media/pi/06A879EAA879D89F/Test/savetxt.csv', data, delimiter=',')  # can see saved csv or txt file and see the 4 columns of data 


b = ti.time()
c = b-a
print("Saving Time =", c)


#LOADING using np.loadtxt()  

#time1,time2,voltage1,voltage2 = pd.read_feather('feather_file')


#LOADING using 

df_read = pd.read_pickle('pickle.pkl') 
print(df_read)      #when you read from a pickle file it adds a column to the left showing the index of each row
                    #it also adds a row to the top to show the index number of each row)

#LOADING using np.loadtxt()  
#time1,time2,voltage1,voltage2 = np.loadtxt('/media/pi/06A879EAA879D89F/Test/savetxt.csv', delimiter=',', unpack=True)
#print(time1,time2,voltage1,voltage2)



#LOADING using np.loadtxt()  
#test = np.load('save.npy') # need to use np.load() to see data wen saved in a .npy file
                                       # unlike savetxt, where you can open the txt or csv file, you need to load the .npy          
#print(test)                            # this should return the same 2D array as data

#NEXT: we need to separate the 2D array into 4 1D arrays that were used to compose it. 

#time1 = [row[0] for row in test]       #time1 is now the same t1, which confirms this method works
#time2 = [row[1] for row in test] 
#voltage1 = [row[2] for row in test]
#voltage2 = [row[3] for row in test]

#print(time1,time2,voltage1,voltage2)


