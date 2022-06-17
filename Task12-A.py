#Составить программу рисования следующей последовательности однотипных фигур

from tkinter import *
window = Tk()
window.title("12")
window.geometry('800x600')
okr = Canvas(window, bg='white', width=800, height=600)
okr.pack()
colors = ["#ffcb99", "#feff01", "#01ff00", "#963463", "#808080"]
j=10
for i in range(5):
    okr.create_rectangle(j, j, j + 100, j + 100, fill=colors[i])    
    j += 50
