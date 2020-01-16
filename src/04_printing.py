"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""

x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"
print("Modulo format   -->  x: %2d        y: %.2f        z: %s" % (x,y,z))
# Use the 'format' string method to print the same thing
print("Format method   -->  x: {0:2d}        y: {1:.2f}        z: {2:s}".format(x,y,z))
# Finally, print the same thing using an f-string
print(f"F-String method -->  x: {x}        y: {y:.2f}        z: {z}")