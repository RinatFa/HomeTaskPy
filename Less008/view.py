import json

def get_txt(path):
    f = open(path, 'r', encoding="utf-8")
    data = f.read()  # чтение в переменную
    f.close()
    return data
def wr_txt(path, sStroka):
    with open(path, 'w', encoding="utf-8") as f: # запись
        for i in range(len(sStroka)-1):
            f.write(f'{sStroka[i][0]} {sStroka[i][1]} {sStroka[i][2]} {sStroka[i][3]}\n')
def app_txt(path, sLastName, sFirstName, sPosition, sSalary):
    with open(path, 'a', encoding="utf-8") as f:  # добавление
        f.write(f'{sLastName} {sFirstName} {sPosition} {sSalary}\n')  # 
def wr_csv(path, sStroka):
    with open(path, 'w', encoding="utf-8") as f: # запись
        for i in range(len(sStroka)-1):
            f.write(f'{sStroka[i][0]};{sStroka[i][1]};{sStroka[i][2]};{sStroka[i][3]}\n')
def wr_json(pat1, pat3):
    # import json - модуль
    # Программа на Python для преобразования текстового файла в JSON
    # pat1 - файл, который будет преобразован
    dict1 = {}  # результирующий словарь
    fields = ['lastname', 'firstname', 'position', 'salary']  # поля в файле
    with open(pat1, encoding="utf-8") as f:
        l = 1  # переменная count для создания идентификатора сотрудника
        for line in f:
            # чтение построчно из текстового файла
            description = list( line.strip().split(None, 4))
            # выходные данные см. ниже
            print(description)
            # для автоматического создания идентификатора для каждого сотрудника
            sno ='emp'+str(l)
            i = 0  # переменная цикла
            dict2 = {}  # промежуточный словарь
            while i < len(fields):
                    # создание словаря для каждого сотрудника
                    dict2[fields[i]]= description[i]
                    i = i + 1
            # добавление записи каждого сотрудника в основной словарь
            dict1[sno]= dict2
            l = l + 1      
    out_file = open(pat3, "w", encoding="utf-8")
    json.dump(dict1, out_file, indent = 4)
    out_file.close()
