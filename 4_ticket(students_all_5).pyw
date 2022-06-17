#Создать файл students.txt(3 фамилии, у 1 все 5ки)
#Каталог D:\students.txt(на латинском всё)
file=open("D:\students.txt","r")
assesment=0
for row in file:
    for symbol in row:
        if symbol=="5":
            assesment=assesment+1
            if assesment==3:
                print(row)
                break
file.close