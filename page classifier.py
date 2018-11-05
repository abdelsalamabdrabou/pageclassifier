import sorting

# Import data from files #
common = open("common.txt", 'r')
commonText = common.read().split(",")
page = open("page1.txt", 'r')
pageText = page.read().lower().split()
pageText = sorting.removePun(pageText)

# Final list #
finalText = {}

# Check if the item is not be found in common words #
for item in pageText:
    if item not in commonText and item != '':
        #  Check item did not repeat# #
        if item in finalText:
            finalText[item] += 1
        else:
            finalText[item] = 1

# Calling algorithms functions  #

#sorting.bubbleSort(finalText)
#sorting.selectionSort(finalText)
#sorting.insertionSort(finalText)
#sorting.mergeSort(finalText)
#sorting.quickSort(finalText)













