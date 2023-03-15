import sys
# import numpy as np
import random
  

num_simulations=[]

for line in sys.stdin:
    line=line.strip()
    line = line.split()
    num_simulations=[int(i) for i in line]
    list=[]
    for i in range(num_simulations[0]):
        x=0
        j=0
        while x<=1:
            x=x+random.uniform(0, 1)
            j=j+1
        list.append(j)
    d={x:list.count(x) for x in list}
    for key, value in d.items():
        print ("% d % d"%(key, value))

        
    

