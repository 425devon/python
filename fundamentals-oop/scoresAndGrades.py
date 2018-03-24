from random import *

def scores():
    count = 0
    print "Scores and Grades"

    while count <= 10:
        grade = randint(60,100)
        if grade >= 60 and grade <= 69:
            print "Score: {};".format(grade), "Your grade is D"
            count +=1
        elif grade >= 70 and grade <= 79:
            print "Score: {};".format(grade), "Your grade is C"
            count +=1
        elif grade >= 80 and grade <= 89:
            print "Score: {};".format(grade), "Your grade is B"
            count +=1
        else:
            print "Score: {};".format(grade), "Your grade is A"
            count +=1
    print "End of program. Bye!~"       
scores()