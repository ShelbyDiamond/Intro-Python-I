"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE
import os
path = os.path.dirname(os.path.realpath(__file__))
foo = open(f"{path}/foo.txt", "r")
print(foo.read())

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
bar = open(f"{path}/bar.txt", "w")
bar.write("This is Bentley\nBentley is my sweet little puppy\nI love Bentley")
bar.close()
