
'''
def odd_even():
    test = (list(range(1,2001)))

    for i in test:
        if(i % 2 != 0):
            print "Number is {}".format(i), "This is an odd number."
        else:
            print "Number is {}".format(i), "This is an even number."

odd_even()
'''
'''
def mult_five(arr, mult):
    for x in range(len(arr)):
        arr[x] *= mult
    print arr
    return arr
mult_five([2,4,10,16], 5)
'''

def layered_multiples(arr, mult):
    answers = []
    for x in range(len(arr)):
        arr[x] *= mult
    for x in range(len(arr)):
        numlist = []
        count = 0
        while count < arr[x]:
            numlist.append(1)
            count +=1
        answers.append(numlist)
    print answers
layered_multiples([2,4,6],2)