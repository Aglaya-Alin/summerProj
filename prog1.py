import codecs
import re
from fuzzywuzzy import fuzz
from thefuzz import process
#pip3 install pip install thefuzz - needde to be installed



with codecs.open("war_and_peace.txt", "r", "utf-8") as file:
    def main(file):
        listOfNames = []
        dict = {}
        for line in file:
            res = re.findall(r"(?<![.\–!?]\s)(?<!…\s)(?<!\[)(?<!\]\s)(?<!^)(?<!«)\b[А-Я][а-я]{3,}\b(?:\s+[А-Я][а-я]*)?\b(?:\s+[А-Я][а-я]*)?\b", line)#тк за тектом на французском идет перевод на русский, то нету смысла искать имена на фр.
            listOfNames += res
            #for i in res:
            #    if i == 'Грунт':
            #        print(line)



        for i in listOfNames:
            if dict.get(i):
                dict[i] += 1
            else:
                dict[i] = 1
        dict2 = {k: v for k, v in dict.items() if v > 1}
        dict3 = {}

        print(len(dict), len(dict2))
        for i in dict2:
            dict3[i] = list()
            for j in dict2:
                #if i != j:
                if fuzz.ratio(i, j) >70:
                    dict3[i].append(j)

        for i in list(dict3.keys()):
            if fuzz.ratio(i,'Париж') > 70:
                del dict3[i]
            elif fuzz.ratio(i,'Москва') > 70:
                del dict3[i]
            elif fuzz.ratio(i,'Европа') > 70:
                del dict3[i]
            elif fuzz.ratio(i,'Австрия') > 70:
                del dict3[i] 
            elif fuzz.ratio(i,'Пруссия') > 70: 
                del dict3[i]
            elif fuzz.ratio(i,'Вена') > 70:
                del dict3[i]
            elif fuzz.ratio(i,'Петербург') > 70:
                del dict3[i]
            elif fuzz.ratio(i,'Франции') > 70:
                del dict3[i]
            elif fuzz.ratio(i,'Россия') > 70:
                del dict3[i]

        print(dict3, len(dict3))
        #print(dictOfNamesRep)
        #for i in dict3:
        #    if len(i.split()) < k: for k in 




    main(file)
