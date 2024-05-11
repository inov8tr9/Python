# updating line 1 as version control tester
#
# ########  4.1.6.1.  here  ###################

tuple1 = (1, 2, 4, 8)
tuple2 = 1., .5, .25, .125

print(tuple1)
print(tuple2)

emptyTuple = ()

oneElementTuple1 = (1, )
oneElementTuple2 = 22.,

print(oneElementTuple2)
print('')
###########################  4.1.6.2 here   ###############

myTuple = (1, 10, 100, 1000)

print(myTuple[0])
print(myTuple[-1])
print(myTuple[1:])
print(myTuple[:-2])
print('')

for elem in myTuple:
    print(elem)
print("")

########################  4.1.6.3  here   #########################

newTuple = (1, 10, 100)

t1 = newTuple + (1000, 10000)
t2 = newTuple * 3

print(len(t1))
print(len(t2))
print(t1)
print(t2)
print(10 in newTuple)
print((-10 not in newTuple))
print('')

var = 123
t1 = (1, )
t2 = (2, )
t3 = (3, var)  # can contain values or strings
print(t1, t2, t3)
print('')

t1, t2, t3 = t2, t3, t1
print(t1, t2, t3)  # note they now swapped places
