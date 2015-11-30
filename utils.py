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
    print sortedDict
    return sortedDict[-1]

#takes data from a website (done in names.py)
#returns the list of most common first names
#not used
def compareNames(l):
    namesList = []
    for word in l:
        if word in names.getNames():
            namesList.append(word)
    return namesList


    
