import model
import view

def button_click():
    bTxtCsv = True  # True - txt, False - cvs
    sStop = ""
    while sStop == "":
        s1 = "\nВведите режим работы со справочником,  0. Выход из справочника: \n"
        s1 += "  1,2. Загрузка справочника  1. из текста txt  2. из табл. csv\n"
        s1 += "  3. Просмотр всего телефонного справочника\n"
        s1 += "  4. Поиск по Фамилии или выборка по буквам\n"
        s1 += "  5. Поиск по Фамилии и удаление\n"
        s1 += "  6. Добавление Фамилии и телефона\n"
        s1 += "  7,8. Запись справочника  7. в текст txt  8. в табл. csv\n"
        s1 += "  9. Просмотр записи телефонного справочника\n"
        s1 += "Введите цифру: "
        s2 = "Введите натуральное число!"
        s3 = "9"
        numberA = model.InputNumb(s1,s2,s3)
        print()
        if numberA == 0:
            print("  Выход из справочника!")
            exit()
        elif numberA == 1:
            print("  1. Загрузка справочника из текста (txt)")
        elif numberA == 2:
            print("  2. Загрузка справочника из табличного текста (csv)")
        elif numberA == 3:
            print("  3. Просмотр всего телефонного справочника")
        elif numberA == 4:
            print("  4. Поиск телефона по Фамилии или выборка по буквам")
        elif numberA == 5:
            print("  5. Поиск телефона по Фамилии и удаление")
        elif numberA == 6:
            print("  6. Добавление Фамилии и телефона")
        elif numberA == 7:
            print("  7. Запись справочника в текст (txt)")
        elif numberA == 8:
            print("  8. Запись справочника в табличный текст (csv)")
        elif numberA == 8:
            print("  9. Просмотр записи телефонного справочника (csv)")

        path1 = 'TelephDirect.txt'
        path2 = 'TelephDirect.csv'
        path3 = 'TelephDirect2.txt'
        path4 = 'TelephDirect2.csv'
        data = view.get_txt(path1)  # считывание текста
        TelephonBase = data.split('\n')  # строки
        sStroka = [i.split(' ') for i in TelephonBase]  # поля
        data = view.get_csv(path2)  # считывание csv
        TelephonBase = data.split('\n')  # строки
        sStroka2 = [i.split(';') for i in TelephonBase]  # поля
        if numberA == 0:
            break
        elif numberA == 1:
            bTxtCsv = True
        elif numberA == 2:
            bTxtCsv = False
        elif numberA == 3:
            if bTxtCsv:
                model.all_teleph(sStroka)  # весь справ.
            else:
                model.all_teleph(sStroka2)  # весь справ.
        elif numberA == 4:
            if bTxtCsv:
                sStroka5 = model.find_teleph(sStroka)  # поиск по Фамилии
            else:
                sStroka6 = model.find_teleph(sStroka2)  # поиск по Фамилии
        elif numberA == 5:
            if bTxtCsv:
                model.find_teleph(sStroka)  # поиск по Фамилии
                bYN = input('Удалить найденное (да - 1) ?')
                if bYN == 1:
                    model.del_teleph(sStroka)
                view.wr_txt(path3, sStroka)  # запись
            else:   
                model.find_teleph(sStroka2)  # поиск по Фамилии
                bYN = input('Удалить найденное (да - 1) ?')
                if bYN == 1:
                    model.del_teleph(sStroka2)
                view.wr_csv(path4, sStroka2)  # запись
        elif numberA == 6:
            if bTxtCsv:
                print(sStroka)
                sLN = input('Введите Фамилию: ')
                sFN = input('Введите Имя: ')
                sT = input('Введите телефон (например, 915-1234567): ')
                view.wr_txt(path3, sStroka)  # запись
                view.app_txt(path3, sLN, sFN, sT)  # добавление
            else:
                sLastName, sFirstName, sTelephon = model.add_teleph()
                view.wr_csv(path4, sStroka2)  # запись
                print(sStroka2)
                view.app_csv(path4, sLastName, sFirstName, sTelephon)
        elif numberA == 7:
            view.wr_txt(path3, sStroka5)  # запись
            bTxtCsv = True
        elif numberA == 8:
            view.wr_csv(path4, sStroka6)  # запись
            bTxtCsv = False
        elif numberA == 9:  # просмотр
            if bTxtCsv:
                data = view.get_txt(path3)  # считывание текста
                TelephonBase = data.split('\n')  # строки
                sStroka = [i.split(' ') for i in TelephonBase]  # поля
                model.all_teleph(sStroka)
            else:
                data = view.get_csv(path4)  # считывание csv
                TelephonBase = data.split('\n')  # строки
                sStroka2 = [i.split(';') for i in TelephonBase]  # поля
                model.all_teleph(sStroka2)
