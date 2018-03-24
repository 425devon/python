from random import *

def coin_toss(tosses):
    heads = 0
    tails = 0
    attempt = 0
    print "Starting the program..."
    while tosses >0:
        toss = randint(0, 100)
        if toss < 50:
            tails += 1
            tosses -= 1
            attempt += 1
            print "Attempt # {}: Throwing a coin.. It's tails! ... Got {} tail(s) so far and {} head(s) so far".format(attempt,tails,heads)
        else:
            heads += 1
            tosses -= 1
            attempt += 1
            print "Attempt # {}: Throwing a coin.. It's heads! ... Got {} heads(s) so far and {} tails(s) so far".format(attempt,heads,tails)
coin_toss(10)