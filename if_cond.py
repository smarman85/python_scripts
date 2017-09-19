def clinic():
    print "You have just entered the clinic!"
    print "Do you take the door on the left or the right?"
    answer = raw_input("Type left of right").lower()

    if answer == 'left' or answer == 'l':
        print "This is the verbal abuse room you heap of parrot droppings!"
    elif answer == 'right' or answer == 'r':
        print "Of course this is the argumnet room, I told you that already"
    else:
        print "You didn't pick a room"
        clinic()
clinic()
