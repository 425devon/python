aboutMe = {}
aboutMe['name'] = 'Devon'
aboutMe['age'] = 29
aboutMe['country'] = 'USA'
aboutMe['favorite_language'] = 'spanglish'

print aboutMe

def openDict (dic,k):
    print k, dic.get(k,'Not Found')

openDict(aboutMe, 'age')