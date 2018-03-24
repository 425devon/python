words = "It's thanksgiving day. It's my birthday, too!"
print words.find('day')

minmax = [2,54,-1,7,12,98]
print min(minmax)
print max(minmax)

first_last =["hello",2,54,-2,7,12,98,"world"]
print first_last[0], first_last[len(first_last)-1]

newlist = [first_last[0], first_last[len(first_last)-1]]
print newlist

num_list = [19,2,54,-2,7,12,98,32,10,-3,6]
num_list.sort()
print num_list

temp = num_list[0:5]
del num_list[1:5]

num_list[0] = temp
print num_list

