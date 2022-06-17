import random
arr=[]

#Формирование массива
for i in range(0,10):
    element=random.randint(-100,100)
    arr.append(element)

print(arr)

#Удаление отрицательных элементов и замена их нулями
new_el=0
for elem in arr:
    if elem<0:
        arr.remove(elem)
        arr.insert(elem,new_el)

#Удаление нулей вначале и добавление их в конец
for elem in arr:
    if elem==0:
        arr.remove(elem)
        arr.append(new_el)

print(arr)
