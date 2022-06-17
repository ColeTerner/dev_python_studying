#Составить программу рисования следующей последовательности однотипных фигур

from tkinter import *
window = Tk()
window.title("12")
window.geometry('800x600')
okr = Canvas(window, bg='white', width=800, height=600)
okr.pack()
colors = ["#ffcb99", "#ffffff", "#329a67", "#cc99fe", "#7e0100"]
for i in range(5):
    okr.create_oval(i*100+1, 2, (i+1) * 100, 102, fill=colors[i])
