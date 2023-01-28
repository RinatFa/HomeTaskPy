import model
import view

def button_click():
    sStop = ""
    while sStop == "":
        s1 = "\n" + "=" * 45
        s1 += "\nВыберите необходимое действие\n"
        s1 += "  1. Найти сотрудника\n"
        s1 += "  2. Сделать выборку сотрудников по должности\n"
        s1 += "  3. Сделать выборку сотрудников по зарплате\n"
        s1 += "  4. Добавить сотрудника\n"
        s1 += "  5. Удалить сотрудника\n"
        s1 += "  6. Обновить данные сотрудника\n"
        s1 += "  7. Экспортировать данные в формате json\n"
        s1 += "  8. Экспортировать данные в формате csv\n"
        s1 += "  9. Закончить работу\n"
        s1 += "Введите номер необходимого действия: "
        s2 = "Введите натуральное число!"
        s3 = "9"
        numberA = model.InputNumb(s1,s2,s3)
        print()
        if numberA == 9:
            print("  Выход из программы!")
            exit()
        elif numberA == 1:
            print("  1. Поиск сотрудника")
        elif numberA == 2:
            print("  2. Выборка сотрудников по должности")
        elif numberA == 3:
            print("  3. Выборка сотрудников по зарплате")
        elif numberA == 4:
            print("  4. Добавление сотрудника")
        elif numberA == 5:
            print("  5. Удаление сотрудника")
        elif numberA == 6:
            print("  6. Обновление данных сотрудника")
        elif numberA == 7:
            print("  7. Экспорт данных в формате json")
        elif numberA == 8:
            print("  8. Экспорт данных в формате csv")

        path1 = 'CompEmployee.txt'
        path3 = 'CompEmployee.json'
        path4 = 'CompEmployee2.csv'
        data = view.get_txt(path1)  # считывание текста
        EmployeeBase = data.split('\n')  # строки
        sStroka = [i.split(' ') for i in EmployeeBase]  # поля
        if numberA == 9:
            break
        elif numberA == 1:
            iNumb = 0
            sStroka5 = model.find_employ(sStroka, iNumb)  # поиск по Фамилии
        elif numberA == 2:
            iNumb = 2
            sStroka5 = model.find_employ(sStroka, iNumb)  # поиск по Должности
        elif numberA == 3:
            iNumb = 3
            sStroka5 = model.find_employ(sStroka, iNumb)  # поиск по Зарплате
        elif numberA == 4:
            print(sStroka)
            sLN = input('Введите Фамилию: ')
            sFN = input('Введите Имя: ')
            sP = input('Введите должность: ')
            sS = input('Введите зарплату: ')
            view.wr_txt(path3, sStroka)  # запись
            view.app_txt(path3, sLN, sFN, sP, sS)  # добавление
        elif numberA == 5:
            model.find_employ(sStroka)  # поиск по Фамилии
            bYN = input('Удалить найденное (да - 1) ?')
            if bYN == 1:
                model.del_employ(sStroka)
            view.wr_txt(path3, sStroka)  # запись
        elif numberA == 6:
            model.find_employ(sStroka)  # поиск по Фамилии
            sLN = input('Введите Фамилию: ')
            sFN = input('Введите Имя: ')
            sP = input('Введите должность: ')
            sS = input('Введите зарплату: ')
            model.del_employ(sStroka)              # удаление
            view.wr_txt(path3, sStroka)            # запись
            view.app_txt(path3, sLN, sFN, sP, sS)  # обновление
        elif numberA == 7:
            view.wr_json(path1, path3)  # запись в json
        elif numberA == 8:
            view.wr_csv(path4, sStroka)  # запись в csv
