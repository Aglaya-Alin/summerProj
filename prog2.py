import codecs
import re


with codecs.open("war&peace.txt", "r", "utf-8") as f:
    def findDialog():
        VOfDialog = 0
        for line in f:
            dictOfDash = dict()
            list = line.split()
            print(list)
            countDialog = 0
        
            for i in range(0, len(list)):
                if list[i] == '–':
                    print(i, "\t")
                    countDialog+=1
                    dictOfDash[countDialog] = i

            dictOfDash[countDialog+1] = len(list)-1
            print(dictOfDash)
            for i in dictOfDash:
                
                if i < len(dictOfDash):
                    if i%2 != 0:
                        #print(dictOfDash[i+1]-dictOfDash[i]-1, "autor")  else print(dictOfDash[i+1]-dictOfDash[i]-1, "pr rech")
                        VOfDialog += dictOfDash[i+1]-dictOfDash[i]-1
                elif i == len(dictOfDash)-1:
                    if i%2 != 0:
                        VOfDialog = dictOfDash[i+1]-dictOfDash[i]
                        #print(dictOfDash[i+1]-dictOfDash[i], "autor") if i%2 == 0 else print(dictOfDash[i+1]-dictOfDash[i], "pr rech")
        print(VOfDialog, " - v of priamaja rech")                #между последним тире и словом не досчитывается 1 слово, если начинать не с 0 элемента
    findDialog()

""""
описание 
файл открылся, чтобы русский язык понимался ютф8 добавили,
все функция, проходится по линиям файла
сначала рзделяет каждую линию по пробелам
идет цикл фор для создании словаря в котром указано кво тире. ключ номер тире, валюе индекс тире массиве сплитаном
зачем? нбыла идея , что нечтные тире между ними прямая речь, но нет
так затем отдельным шагом добавили в словарь индекс последнего элемента массива-1 (тк лен идет с 1 )
это нужно, чтобы куда то добавить текст между последним тире и концом линии
следующий фор проходиться по словарю и если тире нечетное (ключ) подсчитывает кво слов (эдементов массива) между следующим и текущим значением ключа
чтобы цикл не вышел за пределы словаря написан иф для длины ментше длины словаря
элиф нужен, тк иф удаляет первый элемент как тире, ну а тут уже ужаден ибо лен-1 идет
инт объема находится за предеами фора по проходу по линиям иначе бы он обнуллся и считал знакчение только на каждой строке
"""