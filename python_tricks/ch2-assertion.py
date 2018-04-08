def apply_discount(product, discount):
    price = int(product['price'] * (1.0 - discount))
    assert 0 <= price <= product['price']
    return price

# no matter what discounted price can't be lower than $0 or higher than the original price
shoes = {
    'name': 'Fancy Shoes',
    'price': 14900
    }
print (apply_discount(shoes, 0.25))

print (apply_discount(shoes, 2.0))

"""
Assertions are meant to be internal self-checks for your program. Declaring some conditions as impossible in your code
If one condition doesn't hold that means there is a bug 
if your code is bug free, these conditions won't occure, but if they do it makes debuggin easier
!!! Debugging aid not a mech for handling run-time errors
Assertions are not intended to signal expected error conditions, like a File-Not-Found error, where a user can take 
corrective actions or just try again
"""
