'''
def compareLists(list_one,list_two):
    if cmp(list_one, list_two) == 0:
        print("The lists are the same")
    else:
        print("The lists are not the same")

compareLists(['celery','carrots','bread','milk'],['celery','carrots','bread','cream'])
'''
def compareLong(list1,list2):
    if len(list1) != len(list2):
        print("The lists are not the same.")
    else:
        if list1 == list2:
            print("The lists are the same")
        else:
            print("The lists are not the same.")


compareLong([1,2,5,6,5],[1,2,5,6,5])
    
        