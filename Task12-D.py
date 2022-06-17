#Составить программу рисования следующей последовательности однотипных фигур

from tkinter import *
window = Tk()
window.title("12")
window.geometry('800x600')
okr = Canvas(window, bg='white', width=800, height=600)
okr.pack()
colors = ["#ffffff", "#ffcb99", "#97cc02", "#ff00fe", "#02007d"]
for i in range(5):
    okr.create_rectangle(i*100, 0, (i+1) * 100, 100, fill=colors[i])
