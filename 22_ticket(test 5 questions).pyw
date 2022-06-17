test={"Сколько будет 1x1?":1,"Сколько будет 2x2?":4,"Сколько будет 3x3?":9,"Сколько будет 4x4?":16,"Сколько будет 5x5?":25}

keys=list(test.keys())
values=list(test.values())

assesment=0

for i in range(0,5):
    print(keys[i])
    ans=int(input("Ответ: "))
    if ans==values[i]:
        assesment+=1


print("Ваша оценка: "+str(assesment))



