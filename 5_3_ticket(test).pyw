import random



assesment=0

for i in range(0,10):
    x=random.randint(1,10)
    y=random.randint(1,10)
    print(str(x)+"*"+str(y)+"= ")
    ans=input("Введите ответ: ")
    right_ans=x*y
    ans_int=int(ans)
    if (ans_int==right_ans):
        assesment=assesment+1

if (assesment==10):
    print("Отлично")
elif (assesment==8) or (assesment==9):
    print("Хорошо")
elif (assesment==7) or (assesment==6):
    print("Удовлетворительно")
else:
    print("Плохо")