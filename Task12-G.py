#Составить программу рисования следующей последовательности однотипных фигур

from tkinter import *
window = Tk()
window.title("12")
window.geometry('800x600')
okr = Canvas(window, bg='white', width=800, height=600)
okr.pack()
colors = ["#003466", "#017f02", "#97cb04", "#ffffff"]
for i in range(4):
    okr.create_oval(2, i*100+1, 102, (i+1) * 100, fill=colors[i])
