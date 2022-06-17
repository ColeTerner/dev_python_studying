#Составить программу рисования следующей последовательности однотипных фигур

from tkinter import *
window = Tk()
window.title("12")
window.geometry('800x600')
okr = Canvas(window, bg='white', width=800, height=600)
okr.pack()
colors = ["#fffe9a", "#01ffff", "#2cced1", "#7b047c", "#808080"]
j=400
k=400
for i in range(5):
    okr.create_rectangle(k, j, k + 100, j - 100, fill=colors[i])
    j -= 50
    k +=50
