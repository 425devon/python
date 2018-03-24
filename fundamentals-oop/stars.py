'''
def draw_stars(arr):
    canvas = []
    for i in arr:
        stars = []
        count = 0
        while count < i:
            stars.append("*")
            count +=1
        canvas.append(stars)
    for l in canvas:
        print ''.join(l)


draw_stars([2,4,6])
'''
def draw_list(arr):
    canvas = []
    for i in arr:
        if type(i) == int:
            stars = []
            count = 0
            while count < i:
                stars.append("*")
                count +=1
            canvas.append(stars)
        elif type(i) == str:
            letters = []
            count = 0
            while count < len(i):
                letters.append(i[0].lower())
                count += 1
            canvas.append(letters)
    for l in canvas:
        print ''.join(l)


draw_list([2,'Cat',6,'Rabbit'])



    