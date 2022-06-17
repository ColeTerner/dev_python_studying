import numpy as np

arr=np.random.randint(1,100,size=(3,3))

print(arr)
cost=0
for i in range(0,3):
    for j in range(0,3):
        if i==j:
            if arr[i][j]>cost:
                cost=arr[i][j]
print(cost)

for i in range(0,3):
    for j in range(0,3):
        if arr[i][j]==cost:
            print(str(i+1)+" строка "+str(j+1)+" столбец")
