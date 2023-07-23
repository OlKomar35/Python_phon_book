# Phone book


def menu():
    print()
    print('Для выбора пункта из меню нажмите соответствующую этому пункту цифру ')
    print('1. Открыть файл')
    print('2. Показать контакты')
    print('3. Добавить контакты')
    print('4. Найти контакт')
    print('5. Изменить контакт')
    print('6. Удалить контакт')
    print('7. Сохранить файл')
    print('8. Выход')
    num = int(input('Введите номер меню: '))
    return num


# 1
def open_file():
    dictionary = {}
    with open('phone_book.txt', 'r', encoding="utf-8") as file:
        lines = file.readlines()
        num_lines = len(lines)
        print(f"Количество строк в справочнике: {num_lines}")

        for line in lines:
            phone_person = line.strip().split(';')
            print(phone_person)
            list_ = list()
            list_.append(phone_person[0].strip())
            list_.append(phone_person[2].strip())
            dictionary[phone_person[1].strip()] = list_

    return dictionary


# 2
def view_contact(dict_):
    print()
    for (key, val) in dict_.items():
        list_ = list(val)
        print(list_[0] + " " + key + " " + list_[1])


# 4
def search_contact(surname, dict_):
    for (key, val) in dict_.items():
        list_ = list(val)
        if surname.lower() in list_[0].lower():
            print(list_[0] + " " + key + " " + list_[1])


# 5
def change_contact(msg_old,msg_new, dict_):
    if msg_old in dict_.keys():
       item = dict_.pop(msg_old)
       dict_[msg_new]=list(item)
    else:
        key = get_key(dict_, msg_old)
        item_list = list(dict_.pop(key))
        new_list = [val.replace(msg_old,msg_new) for val in item_list]
        dict_[key] = list(new_list)

    return dict_


# 6
def delete_contact(str_, dict_):
    if str_ in dict_.keys():
        dict_.pop(str_)
    else:
        key = get_key(dict_, str_)
        dict_.pop(key)
    return dict_


# 7
def save_contact(dict_):
    str_ = ''
    for (key, val) in dict_.items():
        list_ = list(val)
        str_ = str_ + list_[0] + ';' + key + ';' + list_[1] + '\n'
    with open('phone_book.txt', 'w', encoding="utf-8") as file:
        file.write(str_)


# 8
def close_contact():
    with open('phone_book.txt', 'r', encoding="utf-8") as file:
        file.close()


def get_key(d, value):
    for k, v in d.items():
        list_ = list(v)
        if value in list_:
            return k


flag = True
flag_open = False
dict_phone = dict()
msg = 'No'
while flag:
    num_menu = menu()
    if num_menu == 1:
        dict_phone = open_file()
        flag_open = True
    elif num_menu == 2 and flag_open:
        view_contact(dict_phone)
    elif num_menu == 3 and flag_open:
        print('Новый контакт: ')
        name = input('Введите фамилию и имя: ')
        phone_number = input('Введите номер телефона: ')
        note = input('Введите примечание: ')
        list_ = list()
        list_.append(name)
        list_.append(note)
        dict_phone[phone_number] = list_
    elif num_menu == 4 and flag_open:
        print()
        search_contact(input('Введите фамилию контакта: '), dict_phone)
    elif num_menu == 5 and flag_open:
        if input('Вы хотите изменить имя: (Yes/No?)') == 'Yes':
            name_old = input('Введите имя которое хотите поменять: ')
            name_new = input('Введите имя на которое хотите поменять: ')
            change_contact(name_old, name_new, dict_phone)
        elif input('Вы хотите изменить номер: (Yes/No?)') == 'Yes':
            number_old = input('Введите номер которое хотите поменять: ')
            number_new = input('Введите номер на которое хотите поменять: ')
            change_contact(number_old, number_new, dict_phone)
        elif input('Вы хотите изменить описание: (Yes/No?)') == 'Yes':
            note_old = input('Введите описание которое хотите поменять: ')
            note_new = input('Введите описание на которое хотите поменять: ')
            change_contact(note_old, note_new, dict_phone)
    elif num_menu == 6 and flag_open:
        msg = input('Введите номер телефона который вы хотите удалить: ')
        delete_contact(msg, dict_phone)
    elif num_menu == 7 and flag_open:
        save_contact(dict_phone)
        msg = 'Yes'
    elif num_menu == 8 and flag_open:
        if msg == 'No':
            msg = input(
                'Вы хотите выйти не сохранив( если нажать No, то сохранятся все изменения, а потом файл закроется )?'
                ' (Напишите Yes/No) ')
            if (msg == 'No'):
                save_contact(dict_phone)
        close_contact()
        flag = False
    elif num_menu == 8 and not flag_open:
        close_contact()
        flag = False
    elif not flag_open:
        print()
        print('Файл не открыт! Нажмите 1 для того чтобы открыть файл')
    else:
        print('Введен не верный номер, такого пнукта нет в меню!')
