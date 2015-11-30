import operator, names

#finding the most common element in a list 
def findMostCommonElement(l):
    wordCounter = {}
    for word in l:
        if word in wordCounter:
            wordCounter[word]+=1
        else:
            wordCounter[word]=1
    sortedDict =  sorted(wordCounter.items(), key=operator.itemgetter(1))
    return sortedDict[-1]

def compareNames(l):
    namesList = []
    for word in l:
        if word in names.getNames():
            namesList.append(word)
    return namesList
    
