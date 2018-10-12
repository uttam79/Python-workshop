"""Intro to Python - Part 1 - Hands-On Exercise."""


import math
import random


# TODO: Write a print statement that displays both the type and value of `xy`
xy = math.pi
print("xy is a {} with a value of {}".format(type(xy), xy))


# TODO: Write a conditional to print out if `i` is less than or greater than 150
i = random.randint(0, 200)
if i < 150:
    print("i is less than 150")
elif i == 150:
    print("i is equal to 150")
else:
    print("i is greater than 150")


# TODO: Write a conditional that prints the color of the picked fruit
picked_fruit = random.choice(['strawberry', 'orange', 'banana'])
if picked_fruit == 'orange':
    print("The fruit is orange")
elif picked_fruit == 'strawberry':
    print("The fruit is red")
elif picked_fruit == 'banana':
    print("The fruit is yellow")


# TODO: Write a function that multiplies two numbers and returns the result
def multiply(num1_val, num2_val):
    """Multiply two numbers and return the result."""
    result = num1_val * num2_val
    return result


# TODO: Now call the function a few times to calculate the following answers
print("22 x 86 =", multiply(22, 86))

print("58 x 25 =", multiply(58, 25))

print("294523 * 97423 =", multiply(294523, 97423))