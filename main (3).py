# Reflection:
# Using the math library is more practical because it provides built-in functions
# like sqrt() and pow(), making the program shorter, easier to read, and more accurate.
# Without these functions, calculating the distance would require more complex codes
import math

#Input

x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

#Compute the distance

distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

# Output
print("\nThe distance between the two points is: {:.2f}".format(distance))
