class Customer(object):
    """ produces objects that represent customers."""
    def __init__(self, customer_id):
        self.customer_id = customer_id

    def display_cart(self):
        print("I am a shopping cart!")

class ReturningCustomer(Customer):
    """ For customers that come back"""
    def display_order_history(self):
        print("Order history")

monty = ReturningCustomer("ID: 12345")
monty.display_cart()
monty.display_order_history()
