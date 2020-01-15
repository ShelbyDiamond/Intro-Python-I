# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def is_even(number):
    return number % 2 == 0


# Read a number from the keyboard
number = input("Enter a number: ")
number = int(number)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE
if is_even(number) == True:
    print("Even!")
else:
    print("Odd")