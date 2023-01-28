def get_txt(path):
    f = open(path, 'r', encoding="utf-8")
    data = f.read()  # чтение в переменную
    f.close()
    return data
def wr_txt(path, sStroka):
    with open(path, 'w', encoding="utf-8") as f: # запись
        for i in range(len(sStroka)-1):
            f.write(f'{sStroka[i][0]} {sStroka[i][1]} {sStroka[i][2]}\n')
def app_txt(path, sLastName, sFirstName, sTelephon):
    with open(path, 'a', encoding="utf-8") as f:  # добавление
        f.write(f'{sLastName} {sFirstName} {sTelephon}\n')  # 
def get_csv(path):
    f = open(path, 'r', encoding="utf-8")
    data2 = f.read()  # чтение в переменную
    f.close()
    return data2
def wr_csv(path, sStroka):
    with open(path, 'w', encoding="utf-8") as f: # запись
        for i in range(len(sStroka)-1):
            f.write(f'{sStroka[i][0]};{sStroka[i][1]};{sStroka[i][2]}\n')
def app_csv(path, sLastName, sFirstName, sTelephon):
    with open(path, 'a', encoding="utf-8") as file:
        file.write(f'{sLastName};{sFirstName};{sTelephon}\n')
