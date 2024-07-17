# in-built functions -> functions which are already made

int()
str()
bool()

# Module Functions -> There are various modules which can have various in-built functions which can be used by user just by import that module

import math
print(dir(math))
print()

# user-defined functions

def print_sum(a, b=8):
    c = a+b
    return c

num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))
d = print_sum(num1)
print("Sum of num1 and num2 is : ", d)