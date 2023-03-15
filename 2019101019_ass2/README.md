## Assignment 2



Map-Reduce framework using Hadoop streaming
- Keshav bansal 
- Roll Number: 2019101019

### Q2

```
elif i<=A_r:
        j=0
        for x in arr:
            list=[]
            list.append(0)
            list.append(i-1)
            list.append(j)
            list.append(x)
            list.append(B_c)
            string_print=' '.join(map(str,list))
            file2.write(string_print)
            file2.write("\n")
            j=j+1

```
I am using the above snippet to give input to the mapper.
For every line read by a mapper:
1. first value denotes which matrix entry belongs to
2. second and third value denotes the indices
3. fourth value is the value of the entry
4. fifth value is how many times it would be required by the reducer or how many times it would be printed by mapper

The mapper prints pairs in the form ((i,k,j),A[i][j]) and ((i,k,j),B[j][k]). The pairs with the same values of i,j and k would be multiplied in the reducer and taken sum over all values of j as shown below.
```


    if i == cur_index_i and k == cur_index_k:
        if j == cur_index_j:
            sum_for_cell += val * val_for_cell  

    elif i!=cur_index_i or k!=cur_index_k: 
        row += [sum_for_cell] 
        sum_for_cell = 0  

```
Once either the value of i or k changes we have got the sum or the value for C[i][k] and we append this to our row.

We print the entire row every time the i value changes


### Q3

here we just have to read one line from the input which gives us the number of simulations.

once we have the number of simulations, we run a for loop and in that for loop while loop is there where we keep on generating till sum becomes one for the first time.

We store the count of all such n's in the dictionary using following code:
```
for i in range(num_simulations[0]):
        x=0
        j=0
        while x<=1:
            x=x+random.uniform(0, 1)
            j=j+1
        list.append(j)
    d={x:list.count(x) for x in list}
```

Then, we print all the key, value pairs from the dictionary 
the reducer takes all the key value pairs and returns the average of sum of product of key and value using following

```
for line in sys.stdin:
    line=line.strip()
    line=line.split()
    a=[int(i) for i in line]
    # print(a)
    sum=sum+a[0]*a[1]
    count=count+a[1]

print(sum/count)
```
Some results:
```
for num_itr=100
2.945
```
```
for num_itr=500
2.736
```
```
for num_itr=1000
2.721
```

Accuracy can be defined using the error like or by taking average of all the values:

Let's say here, we can take sum of (2.945+2.736+2.721)/3 =8.402/3= 2.800666

Now, relative error = (2.80066-e)/e= 0.03038

Now, error percentage = relative error *100
= 3.038 %

Accuracy= 100 -error percentage= 100-3.038=96.962%