def all_teleph(sStroka):
    print()
    print('*** Просмотр всего справочника ***')
    for i in range(len(sStroka)-1):
        print(f'{sStroka[i][0]} {sStroka[i][1]} {sStroka[i][2]}')
    print(f'*** В справочнике {len(sStroka)-1} телефонов ***')
def find_teleph(sStroka):
    sStroka3 = []
    sIns = input()
    for i in range(len(sStroka)-1):
        if sIns in sStroka[i][0]: 
            sStroka3.append(sStroka[i])
            print(f'{sStroka[i][0]} {sStroka[i][1]} {sStroka[i][2]}')
    print(sStroka3)
    return sStroka3
def del_teleph(sStroka):
    sStroka3 = []
    sIns = input()
    for i in range(len(sStroka)-1):
        if sIns in sStroka[i][0]:
            n = 1
        else: 
            sStroka3.append(sStroka[i])
            print(f'{sStroka[i][0]} {sStroka[i][1]} {sStroka[i][2]}')
    print(sStroka3)
    return sStroka3
def InputNumb(sStr, s2, s3):  # ввод числа
    numberA = " "
    while (type(numberA) != int):
        numberA = input(sStr)
        if (numberA.isdigit() == False):
            print(s2)
        else:
            numberA = int(numberA)
            if (numberA < 0) or (numberA > int(s3)):
                print("Введите число от 1 до " + s3 + " !")
                numberA = " "
    return numberA
