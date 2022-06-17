#11. Составить программу рисования мишени, состоящей из окружностей
#разного цвета.

from tkinter import *
window = Tk()
window.title("Круг")
window.geometry('800x600')
okr = Canvas(window, bg='white', width=800, height=600)
okr.pack()
colors = ["green", "red", "lightblue", "magenta", "yellow", "blue"]
for i in range(1, 7):
    okr.create_oval(200 + i*20, 200 + i*20, 460 - i*20, 460 - i*20,
                    fill=colors[i-1])
