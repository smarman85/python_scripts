from model import Person

def showAllView(list):
    print ('In our db we have {0} users. Here they are:'.format(len(list)))
    for item in list:
        print (item)

def startView():
    print ("MVC - the simplest example")
    print ("Do you want to see everyone in my db?[y/n]")

def endView():
    print ('Goodbye!')
