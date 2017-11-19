from model import Person
import view

def showAll():
    # gets list of all Person objects
    people_in_db = Person.getAll()
    # calls view
    return view.showAllView(people_in_db)

def addUser():
    print ("More to come later")
    #add_pserson = Person.addUser()

def start():
    view.startView()
    user_input = input()
    if user_input == 's':
        return showAll()
    elif user_input == 'a':
        return addUser()
    else:
        return view.endView()

if __name__ == "__main__":
    # running controller function
    start()
