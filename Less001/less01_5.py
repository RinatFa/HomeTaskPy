# Задача_01_5. Напишите программу, которая принимает
# на вход координаты двух точек и находит расстояние
# между ними в 2D пространстве.
# Пример:
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21

# 1. откуда значение
from math import *
def GetValue(text):
    X = " "
    sStr = "Введите значение координаты точки " + text + ": "
    while (type(X) != float):
        X = input(sStr)
        X1 = X
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
            X = float(X)
    return X

# 2. вычисление
def GetDistance(ax, ay, bx, by):
    return sqrt((ay - by) * (ay - by) + (ax - bx) * (ax - bx))

# 3. печать результата
def PrintRes(ax, ay, bx, by, result):
    r = round(result, 3)
    print(f'|A({ax}, {ay}); B({bx}, {by})| = {r}')

ax = GetValue("ax")
ay = GetValue("ay")
bx = GetValue("bx")
by = GetValue("by")
dis = GetDistance(ax, ay, bx, by)
PrintRes(ax, ay, bx, by, dis)
