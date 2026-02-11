#!/usr/bin/env python3

first_digit = int(input("Enter the first number:\n"))
second_digit = int(input("Enter the second number:\n"))

result = first_digit * second_digit

print(f"{first_digit} x {second_digit} = {result}")
if (result > 0):
    print("The result is positive.")
elif (result == 0):
    print("The result is positive and negative.")
else:
    print("The result is negative.")