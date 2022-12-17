# Задача_01_2. Напишите программу для. проверки
# истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
# для всех значений предикат.

# Ввод
# Вычисление
bResult = True
sStr = ""
for X in range(2):
    for Y in range(2):
        for Z in range(2):
            if (not (X or Y or Z)) == 1:
                bLogic = True
            if (not (X or Y or Z)) == 0:
                bLogic = False
            if (not (X or Y or Z)) == -1:
                bLogic = True
            if (not (X or Y or Z)) == -2:
                bLogic = False
            sStr += f'{X}  {Y}  {Z}   -  '
            sStr += str(bLogic) + "    " + str(int((not (X or Y or Z))))
            sStr += " = " + str(int(((not X) and (not Y) and (not Z))))
            if (not (X or Y or Z)) == ((not X) and (not Y) and (not Z)):
                sStr += "  -  Истина!" + "\n"
            else:
                sStr += "  -  Ложь!" + "\n"
                bResult = False
if bResult:
    sStr += "\n" + " " * 10 + "Утверждение истинно!" + "\n"
else:
    sStr += "\n" + " " * 10 + "Утверждение ложно!" + "\n"
# Вывод
print(sStr)
