# Задача: 3. Реализуйте алгоритм перемешивания списка.
# (рандомно поменять местами элементы списка между собой)

from random import randint
# Ввод
X = " "
sStr = "Введите число элементов списка N: "
while (type(X) != int):
    X = input(sStr)
    if (X.isdigit() == False):
        print("Введите натуральное число!")
    else:
        X = int(X)
        if (X < 2):
            print("Введите число больше 1!")
            X = " "
liNumb = list(range(1, X + 1))
for i in range(1, X + 1):
    liNumb[i - 1] = i
# Вывод 1
print(f'Упорядоченный список  ->  {liNumb}')
# Вычисление
for i in range(0, X - 2):
    MyRnd = randint(i + 1, X - 1)
    iTemp = liNumb[MyRnd]
    liNumb[MyRnd] = liNumb[i]
    liNumb[i] = iTemp
# Вывод 2
print(f'Перемешанный список   ->  {liNumb}')
