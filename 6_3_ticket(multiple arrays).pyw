import random
p=[]

for i in range(0,10):
    new_el=[]
    for j in range(0,10):
        number=random.randint(-10,10)
        new_el.append(number)
    p.append(new_el)

print(p)
s=0
num_of_element=0
for element in p:
    num_of_element=num_of_element+1
    for number in element:
        if (number!=0):
            continue
        elif (number==0):
            s=s+1
            if (s==10):
                print(element+" "+str(num_of_element))



