def write_data(info):
    with open("data.txt","a",encoding="utf-8") as file:
        file.writelines("\n" + info)


def delite_data(search):
    with open("data.txt","r",encoding="utf-8") as file:
        lst = file.readlines()
    search_men = dict()
    search_men_1 = 1
    for i, rou in enumerate(lst):
        if search in rou:
            search_men[search_men_1] = i
            print(search_men_1, rou)
            search_men_1 += 1
    if search_men:
        index = int(input("input number"))
        if index in search_men:
            with open("data.txt","w",encoding="utf-8") as file:
                file.writelines([rou for i, rou in enumerate(lst) if search_men[index] != i])
                print("Успешно удалено" )
        else:
            print(" Ошибка ")
    else:
        print("  Такой контакт не найден ")

def change(search):
    with open("data.txt","r",encoding="utf-8") as file:
        num_search = file.readlines()
        num_search_1 = dict()
        num_search_2 = 1
        for i, rou in enumerate(num_search):
            if search in rou:
                num_search_1[num_search_2] = i
                print(num_search_2, rou)
                num_search_2 += 1
        if num_search_1:
            index = int(input(" Выберите контакт "))
            index_1 = input("Имя - ")
            number = num_search[num_search_1[index]].split(";")[-1]
            if index in num_search_1:
                with open("data.txt","w",encoding="utf-8") as file:
                    file.writelines([(rou if num_search_1[index] != i else index_1 + ";" + number ) for i, rou in enumerate(num_search) ])
                    print(" Успешно изменено " )
            else:
                print(" Erorr")
        else:
            print(" Контакт не найден ")






            

         



