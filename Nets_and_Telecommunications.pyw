from tkinter import *

#ФУНКЦИИ
        #Функции show_process(5 этапов)
#1 этап
def first_step():
    #1 этап - добавление весов путей(бесконечностей)
    str="∞"
    c.create_text(350,180,text=str)
    c.create_text(350,380,text=str)
    c.create_text(550,180,text=str)
    c.create_text(550,380,text=str)
    c.create_text(750,280,text=str)

#2 этап
def second_step():
    #2 этап - добавление весов путей B,C
    message1=c.create_rectangle(200,300,220,310)
    message2=c.create_rectangle(200,300,220,310)
    def motion():
        c.move(message1, 1, -1)
        c.move(message2,1,1)
        if (c.coords(message1)[2] < 320) and (c.coords(message2)[2] < 320):
            root.after(10, motion)
        
    motion()
    
    
    c.create_text(360,180,text="(7)")
    c.create_text(250,250,text="7")

    c.create_text(360,380,text="(4)")
    c.create_text(250,385,text="4")

#3 этап
def third_step():
    #3 этап - добавление весов E,F
    message1=c.create_rectangle(400,200,420,210)
    message2=c.create_rectangle(400,400,420,410)
    message3=c.create_rectangle(400,250,420,260)
    def motion():
        c.move(message1, 1, 0)
        c.move(message2,1,0)
        c.move(message3,1,1)
        if (c.coords(message1)[2] < 550) and (c.coords(message2)[2] < 550):
            root.after(10, motion)     
    motion()

    c.create_text(562,180,text="(15)")
    c.create_text(562,380,text="(14)")

    c.create_text(450,220,text="8")
    c.create_text(450,420,text="10")
    c.create_text(450,320,text="20")

#4 этап
def fourth_step():
    message1=c.create_rectangle(550,250,570,260)
    message2=c.create_rectangle(600,200,620,210)
    message3=c.create_rectangle(550,400,570,410)
    message4=c.create_rectangle(600,400,620,410)
    def motion():
        c.move(message1, 0, 1)
        c.move(message2,1,1)
        c.move(message3,0,-1)
        c.move(message4,1,-1)
        if (c.coords(message1)[2] < 730) and (c.coords(message2)[2] < 730):
            root.after(10, motion)     
    motion()

    c.create_text(530,300,text="2")
    c.create_text(650,250,text="3")
    c.create_text(650,400,text="9")

    c.create_text(762,280,text="(18)")

#5 этап - лавинная рассылка обратно!
def fifth_step():
    c.create_text(500,100,text="Лавинная рассылка обратно к маршрутизатору А по тем же маршрутам",font=("Times New Roman",22,"bold"),fill="red")

        #1)Функция создания фигурки маршрутизатора
def create_switch(x,y,label):
    #2 окружности
    c.create_oval(x,y,x+100,y+50)
    c.create_arc(x,y+25,x+100,y+75,start=180,extent=180,style=ARC,outline="black")

    #соединяющие окружности линии
    c.create_line(x,y+25,x,y+50)
    c.create_line(x+100,y+25,x+100,y+50)

    #Крест сверху
    c.create_line(x+10,y+10,x+90,y+40)
    c.create_line(x+90,y+10,x+10,y+40)

    #Текстовый ярлык маршрутизатора
    c.create_text(x+50,y+60,text=label)

        #2)Функция  зарисовки стартовых 6 маршрутизаторов(start)
def start():
    #6 свичей
    create_switch(100,300,"A")
    create_switch(300,200,"B")
    create_switch(300,400,"C")
    create_switch(500,200,"D")
    create_switch(500,400,"E")
    create_switch(700,300,"F")

    #каналы соединения
    c.create_line(200,325,300,225)  #A-B
    c.create_line(200,325,300,425)  #A-C
    c.create_line(400,225,500,225)  #B-D
    c.create_line(400,425,500,425)  #C-E
    c.create_line(600,225,700,325)  #D-F
    c.create_line(600,425,700,325)  #E-F

    c.create_line(350,275,350,400)  #B-C
    c.create_line(550,275,550,400)  #D-E
    c.create_line(387,267,528,403)  #B-E

        #3)Функция анимации принципа работы (show process)
def show_process():
    but1=Button(root,text="1",background="#555",foreground="#ccc",padx="20",pady="8",font=("Times New Roman","16","bold"),command=first_step)
    but1.place(x=50,y=700)
    
    but2=Button(root,text="2",background="#555",foreground="#ccc",padx="20",pady="8",font=("Times New Roman","16","bold"),command=second_step)
    but2.place(x=150,y=700)

    but3=Button(root,text="3",background="#555",foreground="#ccc",padx="20",pady="8",font=("Times New Roman","16","bold"),command=third_step)
    but3.place(x=250,y=700)

    but4=Button(root,text="4",background="#555",foreground="#ccc",padx="20",pady="8",font=("Times New Roman","16","bold"),command=fourth_step)
    but4.place(x=350,y=700)

    but5=Button(root,text="5",background="#555",foreground="#ccc",padx="20",pady="8",font=("Times New Roman","16","bold"),command=fifth_step)
    but5.place(x=450,y=700)
        #4)Функция очистки холста для перерисовки(пункт Clear меню)
def clear():
    c.delete("all")





#Создание граф. окна
root=Tk()
root.title("IS-IS protocol")
root.geometry("1200x800")

#Создание меню из 3 кнопок + его заполнение(с привязкой функций)
main_menu=Menu(root)

main_menu.add_command(label="Start",command=start)                    #привяжи ко всем команды(command=...)
main_menu.add_command(label="Show process",command=show_process)
main_menu.add_command(label="Clear",command=clear)




#Создание чистого холста CANVAS + его позиционирование
c=Canvas(root,width=1100,height=700,bg="white")
c.pack()


#Позиционирование главного меню + зацикливание граф.окна на экране
root.config(menu=main_menu)
root.mainloop()