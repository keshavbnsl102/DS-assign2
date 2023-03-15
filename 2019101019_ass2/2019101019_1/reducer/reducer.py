import sys

cur_index_i=0
cur_index_j=0
cur_index_k=0

row = []
val_for_cell = 0
sum_for_cell = 0


for line in sys.stdin:
    line = line.strip()
    key, value = line.split('\t')
    key=key.split(',')
    # i, k, j = [int(v.strip('()')) for v in key]
    itr=0
    for v in key:
        v=int(v.strip('()'))
        if itr==0:
            i=v
        if itr==1:
            k=v
        if itr==2:
            j=v
        itr+=1
    val = int(value)
    
    if i == cur_index_i and k == cur_index_k:
        if j == cur_index_j:
            sum_for_cell += val * val_for_cell  

    elif i!=cur_index_i or k!=cur_index_k: 
        row += [sum_for_cell] 
        sum_for_cell = 0  

        if i != cur_index_i:
            print(*row, sep=' ')  
            row = []  

    val_for_cell = val
    cur_index_i=i
    cur_index_j=j
    cur_index_k=k  

row += [sum_for_cell]  
print(*row, sep=' ') 