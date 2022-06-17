import numpy as np
import random

s=0
arr=[]

for i in range(0,10):
    arr.append(random.randint(0,100))
    if (i)%2==0:
        s=s+arr[i]
print(arr)
print(s)
