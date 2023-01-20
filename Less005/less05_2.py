# Задача2: Создайте программу для игры с конфетами человек
# против человека. Условие задачи: На столе лежит 100 (2021)
# конфет. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно
# забрать не более чем 28 конфет. Все конфеты оппонента
# достаются сделавшему последний ход. Сколько конфет нужно
# взять первому игроку, чтобы забрать все конфеты у своего
# конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

from random import randint

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

s1 = "\nВведите вариант игры: \n"
s1 += "  1. Игра против игрока\n"
s1 += "  2. Игра против бота\n"
s1 += "  3. Игра против бота с 'интеллектом'\n"
s1 += "  0. Выход из программы\n"
s1 += "Введите цифру: "
s2 = "Введите натуральное число!"
s3 = "3"
numberA = InputNumb(s1, s2, s3)
print()
if numberA == 0:
    print("  Выход из программы!")
    exit()
if numberA == 1:
    print("  1. Игра против игрока!")
elif numberA == 2:
    print("  2. Игра против бота!")
elif numberA == 3:
    print("  3. Игра против бота  с 'интеллектом'!")
print()

if numberA == 1:
    numberHod = randint(1, 2)  # случайные числа от 1 до 2
    print()
    if numberHod == 1 or numberHod == 0:  # 1 или 0 - 1 игрок, 2 - 2 игрок
        numberHod = 2
        print('Начинает игру ПЕРВЫЙ игрок!')
    else:
        numberHod = 1
        print('Начинает игру ВТОРОЙ игрок!')

    iStart = 100  # начальное количество конфет 
    print(f'Начальное количество конфет = {iStart}')
    sStop = ""
    while sStop == "":
        print("Для выхода из игры - введите цифру '0' ")
        print()
        if numberHod == 1:
            numberHod = 2
            print('***** Ход ВТОРОГО игрока *****')
        else:
            numberHod = 1
            print('***** Ход ПЕРВОГО игрока *****')
    
        s1 = "Введите количество взятых конфет: "
        s2 = "Введите натуральное число!"
        s3 = "28"
        numberA = InputNumb(s1, s2, s3)
        iStart -= numberA
        if numberA == 0:
            break
        if (numberA > 0) and (numberA < 29):
            sStr = ' ' * 11 + "Взято конфет = " + str(numberA)
            sStr2 = str(iStart)
        print(sStr)
        print(f'{" " * 10} Осталось конфет = {sStr2}')
        print()
        if iStart <= 0 and numberHod == 1:
            print('Победа ПЕРВОГО игрока!')
            break
        elif iStart <= 0 and numberHod == 2:
            print('Победа ВТОРОГО игрока!')
            break
elif numberA == 2:
    numberHod = randint(1, 2)  # случайные числа от 1 до 2
    print()
    if numberHod == 1 or numberHod == 0:  # 1 или 0 - 1 игрок, 2 - 2 игрок
        numberHod = 2
        print('Начинает игру Игрок!')
    else:
        numberHod = 1
        print('Начинает игру Бот!')

    iStart = 100  # начальное количество конфет 
    print(f'Начальное количество конфет = {iStart}')
    sStop = ""
    while sStop == "":
        print("Для выхода из игры - введите цифру '0' ")
        print()
        if numberHod == 1:
            numberHod = 2
            print('***** Ход Бота *****')
        else:
            numberHod = 1
            print('***** Ход Игрока *****')
    
        if numberHod == 1:
            s1 = "Введите количество взятых конфет: "
            s2 = "Введите натуральное число!"
            s3 = "28"
            numberA = InputNumb(s1, s2, s3)
        elif numberHod == 2:
            numberA = randint(1, 28)  # случайные числа от 1 до 28
        iStart -= numberA
        if numberA == 0:
            break
        if (numberA > 0) and (numberA < 29):
            sStr = ' ' * 11 + "Взято конфет = " + str(numberA)
            sStr2 = str(iStart)
        print(sStr)
        print(f'{" " * 10} Осталось конфет = {sStr2}')
        print()
        if iStart <= 0 and numberHod == 1:
            print('Победа Игрока!')
            break
        elif iStart <= 0 and numberHod == 2:
            print('Победа Бота!')
            break
elif numberA == 3:
    numberHod = randint(1, 2)  # случайные числа от 1 до 2
    print()
    if numberHod == 1 or numberHod == 0:  # 1 или 0 - 1 игрок, 2 - 2 игрок
        numberHod = 2
        print('Начинает игру Игрок!')
    else:
        numberHod = 1
        print('Начинает игру Бот!')

    iStart = 100  # начальное количество конфет 
    print(f'Начальное количество конфет = {iStart}')
    sStop = ""
    while sStop == "":
        print("Для выхода из игры - введите цифру '0' ")
        print()
        if numberHod == 1:
            numberHod = 2
            print('***** Ход Бота *****')
        else:
            numberHod = 1
            print('***** Ход Игрока *****')
    
        if numberHod == 1:
            s1 = "Введите количество взятых конфет: "
            s2 = "Введите натуральное число!"
            s3 = "28"
            numberA = InputNumb(s1, s2, s3)
        elif numberHod == 2:
            numberA = iStart % 29  # 'интеллект' бота
        iStart -= numberA
        if numberA == 0:
            break
        if (numberA > 0) and (numberA < 29):
            sStr = ' ' * 11 + "Взято конфет = " + str(numberA)
            sStr2 = str(iStart)
        print(sStr)
        print(f'{" " * 10} Осталось конфет = {sStr2}')
        print()
        if iStart <= 0 and numberHod == 1:
            print('Победа Игрока!')
            break
        elif iStart <= 0 and numberHod == 2:
            print('Победа Бота!')
            break
print()
print('******* GAME OVER *******')
print()
