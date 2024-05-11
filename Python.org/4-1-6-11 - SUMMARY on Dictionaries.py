farmDict = {
    "cow": "vaca",
    "chicken": "gallina",
    "bull": "toro"
    }
print(farmDict)
print('')

farmDict['pig'] = 'puerco'  # add keypairs or modify values.   CANNOT modify the key, though....
farmDict['rooster'] = 'noisy'
print(farmDict)
print('')

for item in farmDict:  # basically a listing of keys
    print(item)

for key, value in farmDict.items():  # iterate a list using 'items'
    print("Eng/Span ->", key, ":", value)

if 'slob' in farmDict:  # see if a value is in that list
    print("Yes it's in here.")
else:
    print("No, that's not in here.")

copyFarmDict = farmDict.copy()  # COPY a dict to a new one
print('farmDict is :', farmDict)
print('copyFarmDict is; ', copyFarmDict)

del copyFarmDict
print('farmDict is :', farmDict)
# print('copyFarmDict is: ', copyFarmDict)  # THIS fails because its been deleted.

