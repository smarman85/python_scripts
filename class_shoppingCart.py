class ShoppingCart(object):
    """ Creates shopping cart objects for users
    of our fine website"""
    items_in_cart = {}

    def __init__(self, customer_name):
        self.customer_name = customer_name

    def add_item(self, product, price):
        # Add item to card
        if not product in self.items_in_cart:
            self.items_in_cart[product] = price
            print product + " added to cart."
        else:
            print product + " is already in the cart."

    def remove_item(self, product):
        # remove an Item from the cart
        if product in self.items_in_cart:
            del self.items_in_cart[product]
            print product + " removed."
        else:
            print product + " is not in the cart."

my_cart = ShoppingCart("Sean")
print my_cart.items_in_cart
my_cart.add_item("Candy", 1.25)
print my_cart.customer_name + "'s cart :"
print my_cart.items_in_cart
