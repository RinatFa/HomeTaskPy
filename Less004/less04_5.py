# Задача: 1. Даны два файла, в каждом из которых
# находится запись многочлена. Задача - сформировать
# файл, содержащий сумму многочленов.

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
path1 = 'less04_5_1.txt'
path2 = 'less04_5_2.txt'
data = open(path1, 'r')
for sLine1 in data:
    print(f'           {sLine1}')
data.close
data = open(path2, 'r')
for sLine2 in data:
    print(f'           {sLine2}')
data.close
sLine1 = sLine1[:-4]    # исключение ' = 0' 
sLine2 = sLine2[:-4]    # исключение ' = 0'
A1 = sLine1.split('+')    # 1 многочлен
A2 = sLine2.split('+')    # 2 многочлен
for i in range(len(A1)):    # нет крайних пробелов
    A1[i] = A1[i].strip()
for i in range(len(A2)):    # нет крайних пробелов
    A2[i] = A2[i].strip()
# Определение размерности списков
if A1[0].find('^') > 0:   # ax^2 (+ b) = 0
    iDim1 = int(A1[0][A1[0].find('^') + 1:len(A1[0])])
else:
    iDim1 = 1   # ax (+ b) = 0
if A2[0].find('^') > 0:   # ax^2 (+ b) = 0
    iDim2 = int(A2[0][A2[0].find('^') + 1:len(A2[0])])
else:
    iDim2 = 1   # ax (+ b) = 0
iDim = iDim1
if (iDim < iDim2):
    iDim = iDim2
N = [0] * (iDim + 1)    # размер списка Степень
A = [0] * (iDim + 1)    # размер списка Коэффициенты
for i in range(iDim + 1):
    N[i] = iDim - i
# print(N)
for i in range(len(A1)):    # 1 многочлен
    if A1[i].find('^') > 0:   # для не (1 и 0) степеней х
        iStep = int(A1[i][A1[i].find('^') + 1:len(A1[i])])
        if A1[i].find('*') > 0:
            iKoeff = int(A1[i][:A1[i].find('*')])
        else:
            iKoeff = 1
        A[iDim - iStep] = iKoeff
    elif A1[i][-1] == 'x':
        if A1[i].find('*') > 0:   # для 1 степени х
            iKoeff = int(A1[i][:A1[i].find('*')])
        else:
            iKoeff = 1
        A[iDim - 1] = iKoeff
    elif A1[i].find('x') < 0:   # для 0 степени х
        iKoeff = int(A1[i])
        A[iDim] = iKoeff
# print(A)
for i in range(len(A2)):    # 2 многочлен суммируется
    if A2[i].find('^') > 0:   # для не (1 и 0) степеней х
        iStep = int(A2[i][A2[i].find('^') + 1:len(A2[i])])
        if A2[i].find('*') > 0:
            iKoeff = int(A2[i][:A2[i].find('*')])
        else:
            iKoeff = 1
        A[iDim - iStep] += iKoeff
    elif A2[i][-1] == 'x':
        if A2[i].find('*') > 0:   # для 1 степени х
            iKoeff = int(A2[i][:A2[i].find('*')])
        else:
            iKoeff = 1
        A[iDim - 1] += iKoeff
    elif A2[i].find('x') < 0:   # для 0 степени х
        iKoeff = int(A2[i])
        A[iDim] += iKoeff
# print(A)
# Вычисление
sPolynomial = Polynomial(A, N, iDim)
# Вывод
print(f'k={iDim}  =>  {sPolynomial}')
print('Записано в файл less04_5.txt')
path = 'less04_5.txt'   # Запись в файл .txt
with open(path, 'w') as data:
    data.writelines(f'Stepen        = {N}\n')
    data.writelines(f'Koeffitsienty = {A}\n')
    data.write('\n')
    data.write(f'k={iDim}  =>  {sPolynomial}')
data.close()
