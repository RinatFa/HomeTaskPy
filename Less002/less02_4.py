# Задача: 2. Задайте список из N элементов, заполненных числами
# из промежутка [-N, N]. Найдите произведение элементов
# на указанных позициях. Позиции хранятся в отдельном списке
# ( пример n=4, lst1=[4,-2,1,3] - списко на основе n,
#  а позиции элементов lst2=[3,1].

from random import randint
# Ввод 1
X = " "
sStr = "Введите число N: "
while (type(X) != int):
    X = input(sStr)
    if (X.isdigit() == False):
        print("Введите натуральное число!")
    else:
        X = int(X)
        if (X < 1):
            print("Введите число больше 0!")
            X = " "
# Ввод 2
X2 = " "
sStr = "Введите позицию 1 (от 0 до " + str(X - 1)  + "): "
while (type(X2) != int):
    X2 = input(sStr)
    if (X2.isdigit() == False):
        print("Введите натуральное число!")
    else:
        X2 = int(X2)
        if ((X2 < 0) or (X2 > (X - 1))):
            print(f'Введите число от 0 до {X - 1}')
            X2 = " "
# Ввод 3
X3 = " "
sStr = "Введите позицию 2 (от 0 до " + str(X - 1)  + "): "
while (type(X3) != int):
    X3 = input(sStr)
    if (X3.isdigit() == False):
        print("Введите натуральное число!")
    else:
        X3 = int(X3)
        if ((X3 < 0) or (X3 > (X - 1))):
            print(f'Введите число от 0 до {X - 1}')
            X3 = " "
# Вычисление 1
liNumb = list(range(-X, X + 1))
for i in range(1, X * 2 + 1):
    liNumb[i - 1] = i - X - 1
# Вывод 1
# print(f'Упорядоченный список  ->  {liNumb}')
# Вычисление 2
for i in range(0, X * 2 - 2):
    MyRnd = randint(i + 1, X * 2 - 1)
    iTemp = liNumb[MyRnd]
    liNumb[MyRnd] = liNumb[i]
    liNumb[i] = iTemp
# Вывод 2
# print(f'Перемешанный список   ->  {liNumb}')
# Вычисление 3
lst1 = list(range(0, X))
for i in range(0, X):
    lst1[i] = liNumb[i]
lst2 = list(range(0, 2))
lst2[0] = X2
lst2[1] = X3
# Вывод 3
print(f'lst1  =  {lst1}')
print(f'lst2  =  {lst2}')
print(f'Произведение элементов  =  {lst1[lst2[0]] * lst1[lst2[1]]}')
