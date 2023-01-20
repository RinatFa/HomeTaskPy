# Задача3: Создайте программу для игры в ""Крестики-нолики"".

def GamePole(sP):  # прорисовка поля с клетками
    spPole1 = []  
    spPole2 = [] 
    spPole3 = [] 
    iN = 0
    for e in sP:
        iN += 1
        if iN < 4:
            spPole1.append(e)
        elif iN > 6: 
            spPole3.append(e)
        else:
            spPole2.append(e)
    print()
    print(' ' * 8 + '-' * 16)
    print(f'        |1 {spPole1[0]} |2 {spPole1[1]} |3 {spPole1[2]} |')
    print(' ' * 8 + '-' * 16)
    print(f'        |4 {spPole2[0]} |5 {spPole2[1]} |6 {spPole2[2]} |')
    print(' ' * 8 + '-' * 16)
    print(f'        |7 {spPole3[0]} |8 {spPole3[1]} |9 {spPole3[2]} |')
    print(' ' * 8 + '-' * 16)
    print()

def InputNumb(sStr, s2, s3):  # ввод цифры 1-9
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

print()
s1 = "Введите цифру 1 - ПЕРВЫЙ игрок(0) или 2 - ВТОРОЙ игрок(X): "
s2 = "Введите натуральное число!"
s3 = "2"
numberHod = InputNumb(s1, s2, s3)
print()
if numberHod == 1 or numberHod == 0:  # 1 или 0 - 1 игрок, 2 - 2 игрок
    numberHod = 2
    print('Начинает игру ПЕРВЫЙ игрок, записывайте "0" в клетку!')
else:
    numberHod = 1
    print('Начинает игру ВТОРОЙ игрок, записывайте "X" в клетку!')
# sPole = '========='
sPole = '         '
GamePole(sPole)  # запись = в клетку
spNullX = []

sStop = ""
while sStop == "":
    print("Для выхода из игры - введите цифру '0' ")
    if numberHod == 1:
        numberHod = 2
        print('***** Ход ВТОРОГО игрока (X) *****')
    else:
        numberHod = 1
        print('***** Ход ПЕРВОГО игрока (0) *****')
 
    s1 = "Введите цифру, обозначающую клетку: "
    s2 = "Введите натуральное число!"
    s3 = "9"
    numberA = InputNumb(s1, s2, s3)
    if numberA == 0:
        break
    if numberA in spNullX:
        print()
        print('Это поле уже отмечено! Выход из игры.')
        break
    else:
        spNullX.append(numberA)
    if (numberA > 0) and (numberA < 10):
        sStr = "Выбрана " + str(numberA) + " клетка"
    print(sStr)

    spPole = []  # строку в список
    for e in sPole:
        spPole.append(e)
    if numberHod == 1:
        spPole[numberA - 1] = '0' # запись в клетку - в список
    else:
        spPole[numberA - 1] = 'X' # запись в клетку - в список
    sPole = "".join(spPole)  # список в строку
    GamePole(sPole)  # запись 0 или X в клетку

    if sPole[:3] == "000" or sPole[3:6] == "000" or \
        sPole[6:9] == "000" or sPole[0:9:3] == "000" or \
        sPole[1:9:3] == "000" or sPole[2:9:3] == "000" or \
        sPole[0:9:4] == "000" or sPole[2:7:2] == "000":
        print('Победа ПЕРВОГО игрока!')
        break
    elif sPole[:3] == "XXX" or sPole[3:6] == "XXX" or \
        sPole[6:9] == "XXX" or sPole[0:9:3] == "XXX" or \
        sPole[1:9:3] == "XXX" or sPole[2:9:3] == "XXX" or \
        sPole[0:9:4] == "XXX" or sPole[2:7:2] == "XXX":
        print('Победа ВТОРОГО игрока!')
        break
    if len(spNullX) == 9:
        GamePole(sPole)  # запись 0 или X в клетку
        print()
        print('Ничья! Выход из игры.')
        break
print()
print('******* GAME OVER *******')
print()

# поле; 123
#       456
#       789
# print(sPole[:3])     # 123
# print(sPole[3:6])    # 456
# print(sPole[6:9])    # 789
# print(sPole[0:9:3])  # 147
# print(sPole[1:9:3])  # 258
# print(sPole[2:9:3])  # 369
# print(sPole[0:9:4])  # 159
# print(sPole[2:7:2])  # 357
