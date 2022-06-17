arr=[]

for i in range(0,100):
    arr.append(i+1)

print(arr)

s=0
for element in arr:
    if (element%2)==0:
        s=s+element

print(s)
