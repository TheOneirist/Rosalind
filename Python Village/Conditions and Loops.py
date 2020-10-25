# Sum all the odd numbers between a and b, inclusive
def introP4(a, b):

    i = a
    total = 0

    while i <= b:
        if i % 2 == 1:
            total += i
        i += 1

    return total