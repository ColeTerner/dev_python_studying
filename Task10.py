#10. Построить окружность, состоящую из 6 секторов, раскрашенных в
#разные цвета.

from tkinter import *
window = Tk()
window.title("Круг")
window.geometry('300x300')
okr = Canvas(window, bg='white', width=300, height=300)
okr.pack()
colors = ["green", "red", "lightblue", "magenta", "yellow", "blue"]
for i in range(6):
    j = 60*i
    okr.create_arc(100, 100, 250, 250, start=j, extent=60, fill=colors[i])
