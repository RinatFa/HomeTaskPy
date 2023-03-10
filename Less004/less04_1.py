# Задача: 1. Вычислить число c заданной точностью d
# Пример:
# при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

# Ввод
# Число Пи до 15 знаков:
fPi = 3.141592653589793
print(f'Число Пи до 15 знаков = {fPi}')
# Вычисление и Вывод
for i in range(1, 11):
    d = 1/(10**(i))
    print('d = ' + "{:<12.{n}f}".format(d, n=i), end=",   ")
    # fPi_d = round(fPi, i)             # d = 0.001, π = 3.142
    fPi_d = int(fPi * (10**i))/(10**i)  # d = 0.001, π = 3.141
    print('π = ' + str(fPi_d))
    