# Задача1: Напишите программу, удаляющую из текста все
# слова, содержащие ""абв"".

sStr = 'телепередача абвгдейка - детская образабвовательная \
телевизабвионная программа для дошкольников и младабвших школьников'
print(sStr)
print('без слов с "абв":')
spStr = sStr.split(' ')
sStr = ""
for e in spStr:
    if not 'абв' in e:
        sStr += e + " "
sStr = sStr[:-1]
print(sStr)
