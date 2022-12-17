# Задача_01_1. Напишите программу, которая принимает на вход
# цифру, обозначающую день недели, и проверяет, является ли
# этот день выходным.
# Пример:
# 6 -> да
# 7 -> да
# 1 -> нет

# Ввод
# numberA = int(input('Введите цифру, обозначающую день недели: '))

numberA = " "
sStr = "Введите цифру, обозначающую день недели: "
while (type(numberA) != int):
    numberA = input(sStr)
    if (numberA.isdigit() == False):
        print("Введите натуральное число!")
    else:
        numberA = int(numberA)
        if (numberA < 1) or (numberA > 7):
            print("Введите число от 1 до 7!")
            numberA = " "

# Вычисление
if (numberA > 0) and (numberA < 6):
    sStr = "Рабочий день"
elif (numberA == 6) or (numberA == 7):
    sStr = "Выходной день"
# Вывод
print(sStr)
