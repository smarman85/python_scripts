from model import Person
import view

def showAll():
    # gets list of all Person objects
    people_in_db = Person.getAll()
    # calls view
    return view.showAllView(people_in_db)

def start():
    view.startView()
    user_input = input()
    if user_input == 'y':
        return showAll()
    else:
        return view.endView()

if __name__ == "__main__":
    # running controller function
    start()
