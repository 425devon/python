
mixedList = ['magical unicorns', 19, 'hello', 98.98, 'world']
 
intList = [2, 3, 1, 7, 4, 12]
 
strList = ['magical', 'unicorns']
 
def aboutList(mylist):

    types = []
    strings =[]
    num = 0

    for item in mylist:
        itemtype = type(item)
        if itemtype not in types:
            types.append(itemtype)
        if itemtype == str:
            strings.append(item)
        elif itemtype == int or itemtype == float:
            num += item
    if len(types) > 1:
        print("The list you entered is of mixed type")
        print('String: {}'.format(' '.join(strings)))
        print('Sum: {}'.format(num))
    elif types[0] == int:
        print("The list you entered is of integer type")
        print('Sum: {}'.format(num))
    else:
        print("The list you entered is of string type")
        print('String: {}'.format(' '.join(strings)))
    

aboutList(strList)

