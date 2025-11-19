#https://github.com/jperezmachin/lab11-JP-PN
#Partner 1: Prisha Narne
#Partner 2: Julio Perez
import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero"

def logarithm(a, b):
    if a <= 0 or b <= 0:
        return "Logarithm inputs must be positive"
    
    if a == 2 and b == 2:
        return 4

    return math.log(b, a)

def exp(a, b):
    return a**b

def sqrt(a):
    if a < 0:
        return "Square root inputs must be positive"
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)


