import math
<<<<<<< HEAD
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

# First example
def add(a, b): 
    return a + b
=======

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def logarithm(a, b):
    if a <= 0 or b <= 0:
        raise ValueError("Logarithm inputs must be positive")
    return math.log(b, a)

def exponent(a, b):
    return a**b
>>>>>>> 4dfac547a922e661f0cbcffb133a9e10b98b13f1

def sub(a, b): 
    return a - b

def mul(a, b): 
    return a * b

def div(a, b): # raise ZeroDivisionError if a == 0
    if a == 0:
        raise ZeroDivisionError

    return b/a

def log(a, b):# use math library + raise ValueError
    if a <= 0 or b <= 0:
        raise ValueError("Logarithm inputs must be positive.")
    return math.log(b, a)  # log base a of b

def exp(a, b):
    return a ** b