#Составить программу рисования следующей последовательности однотипных фигур

from tkinter import *
window = Tk()
window.title("12")
window.geometry('800x800')
okr = Canvas(window, bg='white', width=800, height=800)
okr.pack()
colors = ["#ffffff", "#9acb00", "#f96a04", "#993400"]
j=10
for i in range(4):
    okr.create_rectangle(j, j, j+i*50 + 100, j+i*50 + 100, fill=colors[i])    
    j += 30
