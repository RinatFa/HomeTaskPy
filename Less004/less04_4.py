# Задача: 3. Задана натуральная степень k. Сформировать
# случайным образом список коэффициентов (значения от 0
# до 100) многочлена и записать в файл многочлен степени k.
# Пример:
#  k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint
def Polynomial(B, M, L):    # вывод многочлена
    sStr = " "
    for i in range(L+1):
        if ((B[i] > 1) and (M[i] > 1)):
            sStr += " + " + str(B[i]) + "*x^" + str(M[i])
        elif ((B[i] > 1) and (M[i] == 1)):
            sStr += " + " + str(B[i]) + "*x"
        elif ((B[i] > 1) and (M[i] == 0)):
            sStr += " + " + str(B[i])
        elif ((B[i] == 1) and (M[i] > 1)):
            sStr += " + " + "x^" + str(M[i])
        elif ((B[i] == 1) and (M[i] == 1)):
            sStr += " + " + "x"
    sStr += " = 0"
    sStr = sStr[3:]    # исключается первый '+'
    return sStr
# Ввод
K = " "
sStr = "Введите натуральную степень k: "
while (type(K) != int):
    K = input(sStr)
    if (K.isdigit() == False):
        print("Введите натуральное число!")
    else:
        K = int(K)
        if (K < 1):
            print("Введите число больше 0!")
            K = " "
N = []
A = []
# Вычисление
for i in range(K + 1, 0, -1):
    N.append(i - 1)    # Список степеней
for i in range(0, K + 1):
    MyRnd = randint(0, 100)
    A.append(MyRnd)    # Список коэффициентов
sPolynomial = Polynomial(A, N, K)
# Вывод
print(f'k={K}  =>  {sPolynomial}')
print('Записано в файл less04_4.txt')
path = 'less04_4.txt'   # Запись в файл .txt
with open(path, 'w') as data:
    data.writelines(f'Stepen        = {N}\n')
    data.writelines(f'Koeffitsienty = {A}\n')
    data.write('\n')
    data.write(f'k={K}  =>  {sPolynomial}')
data.close()
