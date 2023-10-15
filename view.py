def select_op():
    op = int(input("1.Добавить контакт\n2.Удалить контакт\n3.Изменить имя контакта\nвыбирай то, что хочешь "))
    return op

def get_info():
    fio = input("Напишите имя, фамилию, отчество - ")
    tel = input('Напишите номер телефона - ')
    data = fio + " " + ";" + tel
    return data

def delit_data():
    serach = input("Напишите некоторые данные - ")
    return serach  

def change_data():
    serach = input("Напишите имя контакта - ")
    return serach 
def show_men():
    show = print("Список контактов \n")
    return show
