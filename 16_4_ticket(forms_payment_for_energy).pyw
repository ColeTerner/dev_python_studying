from tkinter import *
from tkinter import messagebox
from tokenize import String
  
#ФУНКЦИЯ РАССЧЕТА
def calc(old_c,new_c,tarif):
    if tarif=="1":
        cost=cost_1
    else:
        cost=cost_2
    old_c=int(old_c)
    new_c=int(new_c)
    kvats=(new_c-old_c)
    exodus=round(kvats*cost,1)
    messagebox.showinfo("ИТОГО",str(exodus)+"KWt")


#ПАРАМЕТРЫ ГРАФИЧЕСКОГО ОКНА
root=Tk()
root.geometry("800x800+600+100")
root.title("CALCULATOR_OF_ENERGY")

#СЧЕТЧИКИ



cost_1=100  #Цена по тарифу
cost_2=200

#РАЗМЕЩЕНИЕ ЯРЛЫКОВ 
old_kvt_label = Label(text="Введите старые показания:")
new_kvt_label = Label(text="Введите новые показания: ")
tarif_label = Label(text="Введите тариф(1/2):")

old_kvt_label.grid(row=0, column=0, sticky="w")
new_kvt_label.grid(row=1, column=0, sticky="w")
tarif_label.grid(row=2, column=0, sticky="w")

#ПОЛЯ ВВОДА
#(исходные данные из полей)
old_count = ""
new_count = ""
tarif = ""

#(создание и расположение полей ввода)
old_count_entry = Entry(textvariable=old_count)
new_count_entry = Entry(textvariable=new_count)
tarif_entry = Entry(textvariable=tarif)

old_count_entry.grid(row=0,column=1, padx=5, pady=5)
new_count_entry.grid(row=1,column=1, padx=5, pady=5)
tarif_entry.grid(row=2,column=1, padx=5, pady=5)

 
message_button = Button(text="Calculate", command=calc(old_count,new_count,tarif))
message_button.grid(row=2,column=1, padx=5, pady=5, sticky="e")
 
root.mainloop()