# Задача: 1. Задайте натуральное число N. Напишите
# программу, которая составит список простых
# множителей числа N.

def PrimeNumb(B, N):    # получение списка простых чисел
    for i in range(2, N):   # не включая само число
        for j in range(2, i + 1):
            if ((i % j) == 0):
                if j == i:  # если делитель - само число
                    B.append(j)
                break   # выход при первом делителе

def MultiPrime(B, iN):  # вычисление простых множителей
    sStr = ""
    iNumb = iN
    for i in range(len(B)):
        while ((iNumb % B[i]) == 0) and (iNumb > 1):
            iNumb /= B[i]
            sStr += ' x ' + str(B[i])
    if sStr != "":
        sStr += ' = ' + str(iN)
        sStr  = sStr[3:]    # исключается первое 'х'
    else:
        sStr  = "Нет простых множителей!"
    return sStr

# Ввод
X = " "
sStr = "Введите натуральное число N: "
while (type(X) != int):
    X = input(sStr)
    if (X.isdigit() == False):
        print("Введите натуральное число!")
    else:
        X = int(X)
        if (X < 2):
            print("Введите число больше 1!")
            X = " "
A = []
# Вычисление
PrimeNumb(A, X)
# print(A)  # Список простых чисел до N
sMulti = MultiPrime(A, X)
# Вывод
print(sMulti)
# 2*3*5 = 30
# 2*3*13 = 78
# 2*2*2*2*3*3 = 144 (0 сек)
# 2*7*7*23 = 2254 (0 сек)
# 2*7*7*7*11*11 = 83 006 (15 сек)
# 2*2*2*2*3*3*5*7*11*11 = 609 840 (12 мин 8 сек)
