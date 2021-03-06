contacts = [
    {
        "name": "John",
        "phone": "123456"
    },
    {
        "name": "Jane",
        "phone": "564321"
    },
    {
        "name": "Bob",
        "phone": "+1234"
    },
]
 
FORMAT_STR = '{:<15} {:>12}'
 
 
def list(contacts):
    print(FORMAT_STR.format('Name', 'Phone'))
    for contact in contacts:
        print(FORMAT_STR.format(
            contact['name'],
            contact['phone']
        ))
 
 
 
def find(contacts):
    print("Введите имя контакта:")
    name = input("> ")
 
    for contact in contacts:
        if contact['name'] == name:
            print(FORMAT_STR.format(
                contact['name'],
                contact['phone']
            ))
            break
    else: 
        print("Контакт не найден")
 
def delete(contacts):
    print("Введите контакт: ")
    name = input('> ')
    for contact in contacts:
        if contact['name'] == name:
            print("Вы хотите удалить контакт %s (yes/no)?: " % name )
            name_del = input('> ')
            if name_del == 'yes':
               contacts.remove(contact)
               print("Вы удалили контакт %s " % name)
 
 
 
def add(contacts):
    print("Введите имя контакта:")
    name = input("> ")
    print("Введите телефон контакта:")
    phone = input("> ")
    new_contact = {
        'name': name,
        'phone': phone
    }
    contacts.append(new_contact)
    
    print('Контакт сохранён')
 
print("Добро пожаловать в телефонную книгу.")
print("""Введите команду:
* list - чтобы посмотреть список контактов.
* find - найти контакт по имени
* add  - добавить контакт
* del  - удаление контакта
* edit - изменение контакта 
* exit - выход""")
 
while True:
    print("\nВведите команду: ")
    command = input('> ')
    if command == 'list':
        list(contacts)
    elif command == 'find':
        find(contacts)
    elif command == 'add':
        add(contacts)
    elif command == 'del':
        delete(contacts)
    elif command == 'edit': 
        edit(contacts)       
    elif command == 'exit':
        break
    else:
        print("Неизвестная команда")