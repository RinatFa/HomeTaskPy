# Задача: 1. Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.
# Пример:
#  пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def MultiFigure(iN):
    sStr = "[ 1"
    for i in range(2, iN + 1):
        lNumb = 1
        for j in range(1, i + 1):
            lNumb *= j
        sStr += ", " + str(lNumb)
    sStr += " ]"
    return sStr
# Ввод
X = " "
sStr = "Введите число N: "
while (type(X) != int):
    X = input(sStr)
    if (X.isdigit() == False):
        print("Введите натуральное число!")
    else:
        X = int(X)
        if (X < 2):
            print("Введите число больше 1!")
            X = " "
# Вычисление
sMultiFigure = MultiFigure(X)
# Вывод
print(f'{X}  ->  {sMultiFigure}')
