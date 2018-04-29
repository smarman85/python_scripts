squares = [ x * x for x in range(10)]
print(squares)
squares2 = [ x * x for x in range(10) if x % 2 == 0]
print(squares2)
squares3 = [
            x * x
            for x in range(10)
            if x % 3 == 0
            ]
print(squares3)
