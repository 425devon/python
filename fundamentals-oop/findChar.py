

def findChar(li,st):
    newList = []
    for item in li:
        if st in item:
            newList.append(item)
    print newList

findChar(['hello','world','my','name','is','Anna'],'a')