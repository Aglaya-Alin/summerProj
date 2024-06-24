def find(list):


    VOfAutor = 0
    dictOfDash = dict()
    countDialog = 0
    VOfSpeech = 0
      
    for i in range(0, len(list)):
        if list[i] == '–':
            countDialog+=1
            dictOfDash[countDialog] = i

    for i in dictOfDash:
        if i%2 == 0:
            VOfAutor += dictOfDash[i]-dictOfDash[i-1]-1

    VOfSpeech = len(list)-VOfAutor
    return VOfSpeech