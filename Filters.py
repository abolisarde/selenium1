
### Filters

# numList = [10 ,4, 3, 5, 9, 22]
# even = []
# for item in numList:
#     if item % 2 == 0:
#         even.append(item)
# print(even)     #[10, 4, 22]

# ###===================================================
# numList = [10 ,4, 3, 5, 9, 22]
# evens = list(filter(lambda item : item % 2 == 0, numList ))
# print(evens)
# ###===================================================
# numList = [10 ,4, 3, 5, 9, 22]
# odds = list(filter(lambda item : item % 2 == 1, numList ))
# print(odds)

##======================================================

aTemp = "welcome"
even = []
for item in aTemp:
    if item not in ['a', 'e', 'i', 'o', 'u']:
        even.append(item)
print(even)     #['e', 'o', 'e']

# aTemp = "welcome"
# odds = list(filter(lambda item : item in ['a', 'e', 'i', 'o', 'u'], aTemp ))
# print(odds)

# aTemp = "welcome"
# odds = list(filter(lambda item : item not in ['a', 'e', 'i', 'o', 'u'], aTemp ))
# print(odds)


atemp ="automation Testing"
even=[]
for item in atemp:
    if item in ['a','e','i','o','u']:
        even.append(item)
print(even)

even =list(filter(lambda item:item in ['a','e','i','o','u'],atemp))
print(even)


