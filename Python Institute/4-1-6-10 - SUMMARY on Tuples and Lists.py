tup1 = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10  # new tuple, notice each element MUST have a comma or it will be a var
print(type(tup1))
print(8 in tup1)  # check to see if that element is present

for elem in tup1:
    if elem >= 4:
        break
    print(elem)

print(tup1[6])
print(tup1[2:])
print(tup1[-4])
print(len(tup1))

# Extra - convert using 'tuple'

list1 = [2, 4, 6, "string", 74, "hut"]  # created new list
print(list1)
print(type(list1))
list1.insert(0, 99)
print('list1 after the insert is: ', list1)
count6 = list1.count(6)  # specifically count how many times something is in a list
print(count6)

listTuple = tuple(list1)  # created new tuple from contents of list1
print(listTuple)
print(type(listTuple))

revList = list(listTuple)  # created new list from previous tuple
print(type(revList))

seqList = []
for i in range(1, 21):
    seqList.append(i)
print(seqList)

seqList.reverse()  # no args needed
print(seqList)

seqList.reverse()  # flip back to original order
print('seqList reversed back to original order is: ', seqList)
print('')

messList = [2, 66, 4, 14, 28, 5, 8, 276, 786, 9, 38, 21, 109, 2]
print(messList)
cleanlist = messList.sort()
print(messList)
print(cleanlist)

