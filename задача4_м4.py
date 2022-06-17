N=int(input("Введите целое число "))
s=0
d=0
while N>0:
    if d==N:
        break
    d+=1
    if N%d==0 and d<N:
        s+=d
if s==N:
    print("Число является совершенным ")
else:
    print("Число не является совершенным ")
