# write a fibbonaci function
def fibbonaci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibbonaci(n-1) + fibbonaci(n-2)

def add3numbers(a, b, c):
    return a + b + c

def add4numbers(a, b, c, d):
    return a + b + c + d
