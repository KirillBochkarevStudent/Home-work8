# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, и 
# Вы должны реализовать функционал для изменения и удаления данных


def name_data():
    return input('Введите имя: ')

def surname_data():
    return input('Введите фамилию: ')

def patronymic_data():
    return input('Введите отчество: ')

def phone_number_data():
    return input('Введите номер телефона: ')

def address_data():
    return input('Введите адрес: ')

def input_contact():
    name = name_data()
    surname = surname_data()
    patronymic = patronymic_data()
    phone_number = phone_number_data()
    address = address_data()
    return f'{name} {surname} {patronymic}\n{phone_number}\n{address}'

def add_contact():
    contact = input_contact()
    with open('Phonebook.txt', 'a', encoding='utf-8') as data:
        data.write(contact + '\n\n')

def read_file():
    with open('Phonebook.txt', 'r', encoding='utf-8') as data:
        return data.read()
    
def print_contacts():
    data = read_file()
    print(data)
    
def search_contact():
    search = input('Введите данные для поиска: ')
    data = read_file().rstrip()
    if search not in data:
        print('Ошибка! Такого нет!')
    else:
        print(data)

def delete_contacts():
    print("Введите полную запись для однозначной идентификации контакта, который хотите удвлить: ")
    contact = input_contact()
    data = read_file()
    if contact in data:
        with open('Phonebook.txt', 'w', encoding='utf-8') as data2:
            data = data.replace(contact + "\n\n", " ")
            data2.write(data)
    else:
        print('Нет такого контакта')

def izm_contact():
    print("Введите полную запись для однозначной идентификации контакта, который хотите удвлить: ")
    contact = input_contact()
    data = read_file()
    if contact in data:
        print("Введите новую запись: ")
        new_contact = input_contact()
        with open('Phonebook.txt', 'w', encoding='utf-8') as data2:
            data = data.replace(contact, new_contact)
            data2.write(data)
    else:
        print('Нет такого контакта')

def user_interface():
    with open('Phonebook.txt', 'a', encoding='utf-8') as data:
        pass
    cmd = None
    while cmd != '4':
        print('Меню:\n''1. Запись контакта\n''2. Вывести данные на экран\n''3. Поиск контакта\n''4. Удалить контакт\n''5. Изменить контакт\n''6. Выход')
        cmd = input('Введите номер операции: ')
        while cmd not in ('1', '2', '3', '4', '5', '6'):
            print('Некорректный ввод')
            cmd = input('Введите номер операции: ')
        match cmd:
            case '1':
                add_contact()
            case '2':
                print_contacts()
            case '3':
                search_contact()
            case '4':
                delete_contacts()
            case '5':
                izm_contact()
            case '6':
                print('До свидания')
user_interface()