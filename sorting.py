def printResult(s):
    print("#####################")
    print("The most common words:")
    print("Iterative\tWord")
    for most in range(5):
        print(s[most][1], "         ", s[most][0])
    print("#####################")

def removePun(alist):
    for i in range(len(alist)):
        if(    alist[i][-1] == "."
            or alist[i][-1] == ","
            or alist[i][-1] == "-"
            or alist[i][-1] == '"'
            or alist[i][-1] == ")"
            or alist[i][-1] == ":"):
            alist[i] = alist[i][:-1]

        #if alist[i][-2:] == "'s" or alist[i][-2:] == "'d":
        #    alist[i] = alist[i][:-2]

        #if alist[i][-3:] == "'ve" or alist[i][-3:] == "'re" or alist[i][-3:] == "'n't":
        #    alist[i] = alist[i][:-3]

        if alist[i] != "" and (alist[i][0] == "(" or alist[i][0] == '"'):
            alist[i] = alist[i][1:]

    return alist

###################

def bubbleSort(alist):
    dectToList = list(alist.items())
    lenList = len(dectToList)

    exchange = False
    for i in range(lenList - 1, 0, -1):
        for j in range(i):
            if dectToList[j][1] < dectToList[j + 1][1]:
                dectToList[j], dectToList[j + 1] = dectToList[j + 1], dectToList[j]
                exchange = True

        if exchange == False:
            break

    printResult(dectToList)

###################

def selectionSort(alist):
    dectToList = list(alist.items())
    lenList = len(dectToList)

    for i in range(lenList-1):
        max = dectToList[i][1]
        maxposition = i
        for j in range(i+1, lenList):
            if dectToList[j][1] > max:
                max = dectToList[j][1]
                maxposition = j
        dectToList[i], dectToList[maxposition] = dectToList[maxposition], dectToList[i]

    printResult(dectToList)


###################

def insertionSort(alist):
    dectToList = list(alist.items())
    lenList = len(dectToList)

    for index in range(1, lenList):
        currentvalue = dectToList[index]
        position = index

        while position > 0 and dectToList[position-1][1] < currentvalue[1]:
            dectToList[position] = dectToList[position-1]
            position = position-1

        dectToList[position] = currentvalue

    printResult(dectToList)

###################

def mergeAlg(alist):

    if len(alist) > 1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeAlg(lefthalf)
        mergeAlg(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i][1] > righthalf[j][1]:
                alist[k] = lefthalf[i]
                i = i + 1
            else:
                alist[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j + 1
            k = k + 1

    return alist

def mergeSort(content):
    dectToList = list(content.items())
    printResult(mergeAlg(dectToList))

###################

def quickSort(alist):
    dectToList = list(alist.items())
    result = quickSortHelper(dectToList, 0, len(alist) - 1)
    printResult(result)


def quickSortHelper(alist, first, last):
    if first < last:
        splitpoint = partition(alist, first, last)
        quickSortHelper(alist, first, splitpoint - 1)
        quickSortHelper(alist, splitpoint + 1, last)

    return alist


def partition(alist, first, last):
    pivotvalue = alist[first][1]
    leftmark = first + 1
    rightmark = last
    done = False
    while not done:
        while leftmark <= rightmark and alist[leftmark][1] >= pivotvalue:
            leftmark = leftmark + 1
        while alist[rightmark][1] <= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1

        if rightmark < leftmark:
            done = True
        else:
            alist[leftmark], alist[rightmark] = alist[rightmark], alist[leftmark]

    alist[first], alist[rightmark] = alist[rightmark], alist[first]

    return rightmark