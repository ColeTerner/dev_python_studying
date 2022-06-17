#Составить программу рисования следующей последовательности однотипных фигур

from tkinter import *
window = Tk()
window.title("12")
window.geometry('800x600')
okr = Canvas(window, bg='white', width=800, height=600)
okr.pack()
colors = ["#ffffff", "#ffce00", "#7f8000", "#353396"]
for i in range(4):
    okr.create_rectangle(0, i*100, 100, (i+1) * 100, fill=colors[i])
