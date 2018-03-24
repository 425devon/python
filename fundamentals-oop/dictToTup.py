my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

def dicToTup(dic):
    tupList = list(my_dict.items())
    print tupList
    print type(tupList[0])


dicToTup(my_dict)