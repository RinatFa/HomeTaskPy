# Задача: Реализуйте RLE алгоритм: реализуйте модуль сжатия
# и восстановления данных. 
# Входные и выходные данные хранятся в отдельных текстовых файлах.

# Упаковка  # sStr = 'aaaabbbccccc'  # 4a3b5c
# sStr = 'aaaabbbcccccdddeeeeeeeeeeeeccccbbbbbbdddddddaaaaaaaa'
path = 'fileArText.txt'
data = open(path, 'r')
for sStr in data:
    print(sStr)  # чтение исходного распакованного текста из файла
data.close
sStr2 = ""
sD = ""
iN = 0
iNumb = 0
for e in sStr:
    iNumb += 1
    if e == sD:  # повтор символа
        iN += 1
        if iNumb == len(sStr):  # последний символ
            sStr2 += str(iN) + sD
    else:  # новый символ
        if iN == 0:  # начало строки
            sD = e
            iN = 1
        else:        # внутри строки
            sStr2 += str(iN) + sD
            sD = e
            iN = 1
print(sStr2)  # упакованный текст
print()
data = open('fileArchive.txt', 'w')
data.writelines(sStr2)  # запись упакованного текста в файл
data.close()

# Распаковка текста
sStr2 = ""
path = 'fileArchive.txt'
data = open(path, 'r')
for sStr2 in data:
    print(sStr2)  # чтение упакованного текста из файла
data.close
sStr = ""
sD = ""
iN = 0
iNumb = 0
sNumb = ""
sNumb10 = '0123456789'  # строковые цифры
for e in sStr2:
    if e in sNumb10:  # найдена цифра
        sNumb += e    # в строковое число
    else:
        sStr += e * int(sNumb)  # строка повтора
        sNumb = ""
print(sStr)  # распакованный текст
data = open('fileArText2.txt', 'w')
data.writelines(sStr)  # запись распакованного текста в файл
data.close()
