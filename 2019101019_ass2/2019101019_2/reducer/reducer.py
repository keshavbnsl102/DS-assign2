import sys
# import numpy as np

count=0
sum=0
for line in sys.stdin:
    line=line.strip()
    line=line.split()
    a=[int(i) for i in line]
    # print(a)
    sum=sum+a[0]*a[1]
    count=count+a[1]

print(sum/count)


