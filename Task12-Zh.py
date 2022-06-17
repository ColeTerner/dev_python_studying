#Составить программу рисования следующей последовательности однотипных фигур

from tkinter import *
window = Tk()
window.title("12")
window.geometry('800x600')
okr = Canvas(window, bg='white', width=800, height=600)
okr.pack()
colors = ["#ffffff", "#ffd206", "#32cdc7", "#a12e69", "#810000"]
j=10
for i in range(5):
    okr.create_oval(j, j, j + 100, j + 100, fill=colors[i])    
    j += 30
