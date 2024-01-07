#importing pandas to read the log file
import pandas as pd
#importing numpy to convert the given log file into an array
import numpy as np
#reading the log file
a=pd.read_csv("Log_file.txt",sep=" ",header=None)
#initializing the varialbles required for counting the tasks
count1=0
count2=0
count3=0
#converting into an array
k=np.array(a)
#converting into a list
g = k.tolist()
#using a loop to count the tasks
for i in range(len(g)):
    #using conditional statements to differentiate strings from floats
    if g[i][1]=="waiting":
        count2+=1
        i+=1
    elif g[i][1]!="waiting":
        if type(g[i][1])==float:
            count1+=1
            i+=1
        else:
            count3+=1
            i+=1    
#printing the variables used for counting
print("Count of tasks in running state:",count1)
print("Count of tasks in waiting state:",count2)
print("Count of tasks in scheduled state:",count3)
#Code can also be written using math and regular expressions

