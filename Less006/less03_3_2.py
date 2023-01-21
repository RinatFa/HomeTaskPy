# Задача: 1. Задайте список из вещественных чисел. Напишите
# программу, которая найдёт разницу между максимальным
# и минимальным значением дробной части элементов.
# (если получаются длинные числа после запятой, это нормально
# и особенность данного языка программирования.
# ваш ответ может не совпадать с примером (0,20))
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# Ввод
A = [1.1, 1.2, 3.1, 5, 10.01]
fDivFraction = 0.0
print(f'Список из вещественных чисел A = {A}  =>  ', end='')
# Вычисление
B = [round(A[i] - int(A[i]), 3) for i in range(len(A)) if (round(A[i] - int(A[i]), 3)) > 0]
fDivFraction = max(B) - min(B)
# Вывод
print(fDivFraction)
