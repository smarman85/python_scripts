import timeit
s = "abcdefghijklmnopqrstuvwxyz" * 10

def reverse_string1(s):
    return s[::-1]

def reverse_string2(s):
    return "".join(reversed(s))

def reverse_string3(s):
    chars = list(s)
    for i in range(len(s) // 2):
        tmp = chars[i]
        chars[i] = chars[len(s) - i - 1]
        chars[len(s) - i - 1] = tmp
    return ''.join(chars)

def reverse_string4(s):
    count = len(s) - 1
    new_string = ""
    while count >= 0:
        new_string += s[count]
        count -= 1
    return new_string

print(timeit.repeat(lambda: reverse_string1(s)))

print(timeit.repeat(lambda: reverse_string2(s)))

print(timeit.repeat(lambda: reverse_string3(s)))

print(timeit.repeat(lambda: reverse_string3(s)))
