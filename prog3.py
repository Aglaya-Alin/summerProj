import codecs
import re
from test import find

with codecs.open("war_and_peace.txt", "r", "utf-8") as f:
    def findDialog():
        listofdialog = []
        VOfDialog = 0
        dictOfDash = dict()
        countDialog = 0
        for line in f:
            #print(line)
            list = re.findall(r'«.+»', line)
            if len(list) !=0:
                for i in range(0, len(list)):
                    listofdialog += list[i].split()
                #print(line, "\n", listofdialog, "\n")
        print(listofdialog)
        print(len(listofdialog), " len")
        print(find(listofdialog))  
        
    findDialog()