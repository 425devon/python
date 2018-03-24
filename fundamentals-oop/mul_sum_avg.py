#1
'''
for x in range(1, 1000):
    if x % 2 == 1:
        print x
'''
#2
'''
for x in range(5, 1000000):
    if x % 5 == 0:
        print x
'''
#3

a = [1, 2, 5, 10, 255, 3]
'''
print sum(i for i in a)

#or simply sum(a)
'''
#4
avg = sum(a)/len(a)

print avg