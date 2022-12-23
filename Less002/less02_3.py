# Задача: 1. Задайте список из n чисел последовательности
#  (1+1/n)**n и выведите на экран их сумму.

# Ввод
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
# Вычисление
fSum = 0
liNumb = list(range(1, X + 1))
for i in range(1, X + 1):
    fNumb = (1 + 1 / i) ** i
    liNumb[i - 1] = (str(fNumb)).strip()
    fSum += fNumb
# Вывод
print(liNumb)
print(f'Сумма чисел последовательности  =  {fSum}')
