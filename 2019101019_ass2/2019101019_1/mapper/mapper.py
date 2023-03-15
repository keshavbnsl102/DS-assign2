import sys

for line in sys.stdin:
    # print(line)
    # break
    arr=[int(x) for x in line.strip().split()]
    # print(arr)
    if arr[0]==0:
        for c in range(arr[4]):
            print("%s\t%s" % ((arr[1], c, arr[2] ), arr[3]))
    if arr[0]==1:
        for a in range(arr[4]):
            print("%s\t%s" % ((a, arr[2], arr[1] ), arr[3]))
            





    




