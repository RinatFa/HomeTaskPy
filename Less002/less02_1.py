# Задача: 1. Напишите программу, которая принимает на вход
# вещественное число и показывает сумму его цифр.
# Пример:
#  6782 -> 23
#  0,56 -> 11

def SumFigure(fNumb):
    iSumFigure = 0
    sStr = str(fNumb).strip()
    if ('.' in sStr):
        sStr = sStr.replace(".", "0")
    iNumb = int(sStr)
    for i in range(1, len(sStr) + 1):
        iSumFigure += iNumb % 10
        iNumb //= 10
    return iSumFigure
# Ввод
X = " "
sStr = "Введите вещественное число: "
while (type(X) != float):
    sFlNumber = input(sStr)
    X1 = sFlNumber
    tempX1 = ""
    for s in X1:  # в целое число
        if s != ".":
            tempX1 += s
    X1 = tempX1
    if X1[0] == "-":  # в положит. число
        X1 = X1[1:]
    if (X1.isdigit() == False):
        print("Введите число!")
    else:
        X = float(sFlNumber)
# Вычисление
iSumFigure = SumFigure(abs(X))
# Вывод
print(f'{sFlNumber}  ->  {iSumFigure}')
