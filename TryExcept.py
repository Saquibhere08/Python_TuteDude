
try:
    num1=int(input("Enter a number: "))
    num2=int(input("Enter another Number: "))
    result=num1/num2

    print(result)

except ZeroDivisionError: 
    print("The Denominator cannot be 0")
except ValueError:
    print("Inout should only be in digits")

"""
ZeroDivisionError: In Python, a ZeroDivisionError occurs when you 
try to divide a number by zero, which is mathematically undefined.

ValueError: A ValueError in Python happens when a function or operation receives the right type of argument, 
but the value of that argument is invalid or inappropriate.

"""