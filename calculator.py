# -*- coding: utf-8 -*-
"""Calculator.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jk-L9HJ5tym1unCmogjDEbIb1iu18Ltp
"""

def calculate():
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    operation = input("Choose an operation: add, sub, mul, div: ")
    if operation == "add":
        result = x + y
        
    elif operation == "sub":
        result = x - y
        
    elif operation == "mul":
        result = x * y
       
    elif operation == "div":
        try:
          result = x / y
        except ZeroDivisionError:
            print("Cannot divide by zero.")
            return
    print("Result:", result)
calculate()