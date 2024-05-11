# Exercise 1
# What happens when you attempt to run the following snippet?
myTup = (1, 2, 3)
print(myTup[2])  # you get 3 as its 3rd index elem

# Exercise 2
# What is the output of the following snippet?
tup = 1, 2, 3
a, b, c = tup
print(a * b * c)  # you get 6 because tuples have already been converted to values = simple math now

# Exercise 3
# Complete the code to correctly use the count() method to find the number of duplicates of 2 in the following tuple.
tup = 1, 2, 3, 2, 4, 5, 6, 2, 7, 2, 8, 9
duplicates = tup.count(2)  # your code
print(duplicates)    # outputs: 4

# Exercise 4
# Write a program that will "glue" the two dictionaries (d1 and d2) together and create a new one (d3).
d1 = {'Adam Smith':'A', 'Judy Paxton':'B+'}
d2 = {'Mary Louis':'A', 'Patrick White':'C'}
d3 = {}

for item in (d1, d2):
     # d3.append()  # your code BUT WRONG
     d3.update(item)  # correct way, they gave you 'item' already !!
print(d3)

# Exercise 5
# Write a program that will convert the l list to a tuple.
l = ["car", "Ford", "flower", "Tulip"]
print(l)

t = tuple(l)  # your code = correct
print(t)
print(type(t))

# Exercise 6
# Write a program that will convert the colors tuple to a dictionary.
colors = (("green", "#008000"), ("blue", "#0000FF"))
colDict = dict(colors)  # your code, dict is OK do NOT have to type out 'dictionary'

print(colDict)
print(type(colDict))

# Exercise 7
# What will happen when you run the following code?
myDict = {"A":1, "B":2}
copyMyDict = myDict.copy()  # made a copy of it
myDict.clear()  # cleared out the original one

print(copyMyDict)  # {'A': 1, 'B': 2}  # this is answer.... don't be faked out.
print(myDict)  # this is empty

# Exercise 8
# What is the output of the following program?
colors = {
    "white" : (255, 255, 255),  # this looks like properly constructed Dict
    "grey"  : (128, 128, 128),
    "red"   : (255, 0, 0),
    "green" : (0, 128, 0)
    }

for col, rgb in colors.items():
    print(col, "->", rgb)  # you get a chart... it is accurate.

newListy = []
for i in range(1, 11):
    newListy.append(i)

print(newListy)

for k in range(30, 36):
     newListy.append(k)
print(newListy)

newListy.insert(8, 99)
print(newListy)
print(len(newListy))