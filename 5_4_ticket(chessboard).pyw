import turtle as t
 
step = 40
# t.pensize(3)
 
for i in range (8): # 8 рядов маленьких квадратов
    for j in range(8): # 1 ряд маленьких квадратов
        t.penup()
        t.goto(step * j, step * i)
        t.pendown()
 
        if (i + j) % 2 == 0:
                         t.color ('black', 'black') # Официальный документ: Ссылка 1: Цвет границы, Ссылка 2: Цвет заливки
        else:
            t.color('black', 'white')
 
                 # 1 маленький квадрат
        t.begin_fill()
        for _ in range(4):
            t.forward(step)
            t.left(90)
        t.end_fill()
 
t.done()