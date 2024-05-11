########  4.1.6.4  here   #############

dict = {"cat": "chat", "dog": "chien", "horse": "cheval", 'chicken': 'gallina', 'house': 'casa'}
phones = {'boss': 5551212, 'Suzy': 9544410}
emptyDict = {}

print(dict)
print(phones)
print(emptyDict)
print('')

##############  4.1.6.5  here - calling from a Dict   #########
print(dict['horse'])
print(phones['Suzy'])

### finding stuff  ###

wordsToFind = ['cat', 'lion', 'horse']
for word in wordsToFind:
    if word in dict:
        print(word, "->", dict[word])
    else:
        print(word, 'is not in the dictionary')
print('')
print() # another way to print blank line
print()

###########  4.1.6.6 here - methods on Dictionaries   ########
newDict = {"cat": "chat", "dog": "chien", "horse": "cheval", 'chicken': 'gallina', 'house': 'casa'}

for key in newDict.keys():  # notice method of 'key'
    print(key, "->", newDict[key])
print('')

for key in sorted(newDict.keys()):  # notice method of 'sorted' added to the request
    print(key, "->", newDict[key])
print('')

##########  4.1.6.7 here - more methods on dictionaries    #########
newDict = {"cat": "chat", "dog": "chien", "horse": "cheval", 'chicken': 'gallina', 'house': 'casa'}

for english, french in newDict.items():
    print(english, '->', french)  # notice this prints out key:value PAIRS as TUPLES
print('')
for french in newDict.values():  # notice it prints ONLY the values
    print(french)
print('')

###########  4.1.6.8 here - adding to dictionaries because they are mutable   ##########
newDict = {"cat": "chat", "dog": "chien", "horse": "cheval", 'chicken': 'gallina', 'house': 'casa'}

newDict['cat'] = 'minou'  # change definition of VALUE of a key
print(newDict)
print('')

newDict['swan'] = 'cygne'  # add a new pair
print(newDict)
newDict.update({"duck": "canard"})  # add a new pair using UPDATE method
print(newDict)
print('')

del newDict['swan']  # deleting using the key name
print(newDict)
print('')

newDict.popitem()  # this will pop out and delete LAST pair by default
print(newDict)
