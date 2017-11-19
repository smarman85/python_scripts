from model import Person

def showAllView(list):
    print ('In our db we have {0} users. Here they are:'.format(len(list)))
    for item in list:
        print (item)

def startView():
    print ("MVC - the simplest example")
    print ("""\
What would you like to do:
1. Add a user to the db [a]
2. Show users in the db [s]
3 exit [e] """)

def endView():
    print ('Goodbye!')
