# Задача 01_4. Напишите программу, которая по заданному
# номеру четверти, показывает диапазон возможных координат
# точек в этой четверти (x и y).

# Ввод
iQuarter = " "
sStr = "Введите номер четверти координатной плоскости: "
while (type(iQuarter) != int):
    iQuarter = input(sStr)
    if (iQuarter.isdigit() == False):
        print("Введите натуральное число!")
    else:
        iQuarter = int(iQuarter)
        if (iQuarter < 1) or (iQuarter > 4):
            print("Введите число от 1 до 4!")
            iQuarter = " "
# Вычисление
if iQuarter == 1:
    sStr = "Возможные координаты точек (x, y): x > 0, y > 0"
elif iQuarter == 2:
    sStr = "Возможные координаты точек (x, y): x < 0, y > 0"
elif iQuarter == 3:
    sStr = "Возможные координаты точек (x, y): x < 0, y < 0"
elif iQuarter == 4:
    sStr = "Возможные координаты точек (x, y): x > 0, y < 0"
# Вывод
print(sStr)
