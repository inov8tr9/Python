# -*- coding: utf-8 -*-

# File Name: 2.1.1.10 to
# Author: Educ8tr
# Date: 5/11/2024
# Description: 

# Additional Info:

########  2.1.1.10  here  ###############
# The print() function - instructions
#
# We've changed the example a bit - we've added one empty print() function invocation.
# We call it empty because we haven't delivered any arguments to the function.

print("The itsy bitsy spider climbed up the waterspout.")
print()
print("Down came the rain and washed the spider out.")
print()  # Manually added so we can separate results down the page.

########  2.1.1.11  here  ###############

# The print() function - the escape and newline characters
# The backslash (\) has a very special meaning when used inside strings - this is called the escape character.
# The letter n placed after the backslash comes from the word newline.

print("The itsy bitsy spider\nclimbed up the waterspout.")
print()
print("Down came the rain\nand washed the spider out.")
print()  # Manually added so we can separate results down the page.

########  2.1.1.13  here  ###############

# The print() function - using multiple arguments
# So far we have tested the print() function behavior with no arguments, and with one argument.
# It's also worth trying to feed the print() function with more than one argument.
#
# Look at the editor window. This is what we're going to test now:
#
# print("The itsy bitsy spider" , "climbed up" , "the waterspout.")
#
# There is one print() function invocation, but it contains three arguments. All of them are strings.
#
# The arguments are separated by commas.
# We've surrounded them with spaces to make them more visible, but it's not really necessary.

print("The itsy bitsy spider" , "climbed up" , "the waterspout.")
print()  # Manually added so we can separate results down the page.

########  2.1.1.14  here  ###############

# The print() function - the positional way of passing the arguments

print("My name is", "Python.")
print("Monty Python.")
print()  # Manually added so we can separate results down the page.

########  2.1.1.15  here  ###############

# The print() function - the keyword arguments
# The print() function has two keyword arguments that you can use for your purposes. The first of them is named end.

print("My name is", "Python.", end=" ")
print("Monty Python.")
print()  # Manually added so we can separate results down the page.


########  2.1.1.16  here  ###############

# The print() function - the keyword arguments
# If you look carefully, you'll see that we've used the 'end' argument, but the string assigned to it is empty.
# What will happen now?
# As the end argument has been set to nothing, the print() function outputs nothing too, once its positional arguments have been exhausted.

print("My name is ", end="")
print("Monty Python.")
print()  # Manually added so we can separate results down the page.

########  2.1.1.17  here  ###############

# The print() function - the keyword arguments
# We've said previously that the print() function separates its outputted arguments with spaces.
# This behavior can be changed, too.
# The keyword argument that can do this is named sep (like separator).

print("My", "name", "is", "Monty", "Python.", sep="-")
print()  # Manually added so we can separate results down the page.

########  2.1.1.18  here  ###############

# The print() function - the keyword arguments
# Both keyword arguments may be mixed in one invocation, just like here in the editor window.
# The example doesn't make much sense, but it visibly presents the interactions between end and sep.

print("My", "name", "is", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n")

