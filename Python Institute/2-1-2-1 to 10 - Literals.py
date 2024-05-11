# -*- coding: utf-8 -*-

# File Name: 2-1-2-1 to x - Literals
# Author: Educ8tr
# Date: 5/11/2024
# Description: 

# Additional Info:
# Literals -  And this is the clue: 123 is a literal, and c is not.
#
# You use literals to encode data and to put them into your code.
# We're now going to show you some conventions you have to obey when using Python.





########  2.1.2.2  here  ###############

# Literals - the data in itself
# Let's start with a simple experiment - take a look at the snippet in the editor.
#
# The first line looks familiar. The second seems to be erroneous due to the visible lack of quotes.
# The print() function presents them in exactly the same way

print("2")
print(2)
print()  # Manually added so we can separate results down the page.


########  2.1.2.4  here  ###############

# Integers: octal and hexadecimal numbers
# There are two additional conventions in Python that are unknown to the world of mathematics.
# The first allows us to use numbers in an octal representation.
#
# If an integer number is preceded by an 0O or 0o prefix (zero-o), it will be treated as an octal value.
# This means that the number must contain digits taken from the [0..7] range only.
#
# 0o123 is an octal number with a (decimal) value equal to 83.
#
# The print() function does the conversion automatically. Try this:

print(0o123)

# The second convention allows us to use hexadecimal numbers. Such numbers should be preceded by the prefix 0x or 0X (zero-x).
#
# 0x123 is a hexadecimal number with a (decimal) value equal to 291. The print() function can manage these values too. Try this:

print(0x123)
print()  # Manually added so we can separate results down the page.




########  2.1.2.5  here  ###############

# Floats
# Now it's time to talk about another type, which is designed to represent and to store the numbers that
# (as a mathematician would say) have a non-empty decimal fraction.
#
# They are the numbers that have (or may have) a fractional part after the decimal point, and although
# such a definition is very poor, it's certainly sufficient for what we wish to discuss.
#
# Whenever we use a term like two and a half or minus zero point four, we think of numbers which
# the computer considers floating-point numbers:


########  2.1.2.6.  here  ###############

# Ints vs. floats
# The decimal point is essentially important in recognizing floating-point numbers in Python.
#
# Look at these two numbers: 4 and 4.0
#
# You may think that they are exactly the same, but Python sees them in a completely different way.
#
# 4 is an integer number, whereas 4.0 is a floating-point number.
#
# On the other hand, it's not only points that make a float. You can also use the letter e.
#
# When you want to use any numbers that are very large or very small, you can use scientific notation.
#
#
# Take, for example, the speed of light, expressed in meters per second. Written directly it would look like this: 300000000.
#
# To avoid writing out so many zeros, physics textbooks use an abbreviated form, which you have probably already seen: 3 x 108.
#
# It reads: three times ten to the power of eight.
#
# In Python, the same effect is achieved in a slightly different way - take a look:
#
# 3E8
#
# The letter E (you can also use the lower-case letter e - it comes from the word exponent) is a concise record of the phrase times ten to the power of.
#
# Note:
#
# the exponent (the value after the E) has to be an integer;
# the base (the value in front of the E) may be an integer.



########  2.1.2.7  here  ###############

# Coding floats
# Let's see how this convention is used to record numbers that are very small (in the sense
# of their absolute value, which is close to zero).
#
# A physical constant called Planck's constant (and denoted as h), according to the textbooks, has the value of: 6.62607 x 10-34.
#
# If you would like to use it in a program, you should write it this way:
#
# 6.62607E-34
#
# Note: the fact that you've chosen one of the possible forms of coding float values
# doesn't mean that Python will present it the same way.
#
# Python may sometimes choose different notation than you.
#
# For example, let's say you've decided to use the following float literal:
#
# 0.0000000000000000000001
#
# When you run this literal through Python:
#
# print(0.0000000000000000000001)
#
# this is the result:
#
# 1e-22
# output
#
# Python always chooses the more economical form of the number's presentation,
# and you should take this into consideration when creating literals.


########  2.1.2.8  here  ###############

# Strings
# Strings are used when you need to process text (like names of all kinds, addresses, novels, etc.), not numbers.
#
# You already know a bit about them, e.g., that strings need quotes the way floats need points.
#
# This is a very typical string: "I am a string."
#
#
# However, there is a catch. The catch is how to encode a quote inside a string which is already delimited by quotes.
#
# Let's assume that we want to print a very simple message saying:
#
# I like "Monty Python"
#
# How do we do it without generating an error? There are two possible solutions.
#
#
# The first is based on the concept we already know of the escape character, which you should
# remember is played by the backslash. The backslash can escape quotes too.
# A quote preceded by a backslash changes its meaning - it's not a delimiter, but just a quote.
# This will work as intended:
#
# print("I like \"Monty Python\"")
#
# Note: there are two escaped quotes inside the string - can you see them both?
#
# The second solution may be a bit surprising. Python can use an apostrophe instead of a quote.
# Either of these characters may delimit strings, but you must be consistent.
#
# If you open a string with a quote, you have to close it with a quote.
#
# If you start a string with an apostrophe, you have to end it with an apostrophe.
#
# This example will work too:
#
# print('I like "Monty Python"')
#
# Note: you don't need to do any escaping here.


########  2.1.2.9  here  ###############

# Coding strings
# Now, the next question is: how do you embed an apostrophe into a string placed between apostrophes?
#
# You should already know the answer, or to be precise, two possible answers.
#
# Try to print out a string containing the following message:
#
# I'm Monty Python.
#
# Do you know how to do it? Click Check below to see if you were right:
#
# Check
# print('I\'m Monty Python.')
#
# or
#
# print("I'm Monty Python.")
# As you can see, the backslash is a very powerful tool - it can escape not only quotes, but also apostrophes.
#
# We've shown it already, but we want to emphasize this phenomenon once more - a string can be empty - it may contain no characters at all.
#
# An empty string still remains a string:
#
# ''
# ""


########  2.1.2.10  here  ###############

# Boolean values
# To conclude with Python's literals, there are two additional ones.
#
# They're not as obvious as any of the previous ones, as they're used to represent a very abstract value - truthfulness.
#
# Each time you ask Python if one number is greater than another, the question results in the creation of some specific data - a Boolean value.
#
# The name comes from George Boole (1815-1864), the author of the fundamental work, The Laws of Thought, which contains the definition of Boolean algebra - a part of algebra which makes use of only two distinct values: True and False, denoted as 1 and 0.
#
#
# A programmer writes a program, and the program asks questions. Python executes the program, and provides the answers. The program must be able to react according to the received answers.
#
# Fortunately, computers know only two kinds of answers:
#
# Yes, this is true;
# No, this is false.
# You'll never get a response like: I don't know or Probably yes, but I don't know for sure.
#
#
# Python, then, is a binary reptile.
#
# These two Boolean values have strict denotations in Python:
#
# True
# False
#
# You cannot change anything - you have to take these symbols as they are, including case-sensitivity.
#
#
# Challenge: What will be the output of the following snippet of code?

print(True > False)
print(True < False)

# Run the code in the Sandbox to check. Can you explain the result?









########  2.1.2.  here  ###############








########  2.1.2.  here  ###############