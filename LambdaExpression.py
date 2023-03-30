
# def isAdult(age):
#     if age > 18:
#         return True
#     else:
#         return False

# print(isAdult(30))      #True


# ###===================================================

# isAdultBoolean = lambda age : age > 18
# print(isAdultBoolean(20))       #True

# ###====================================================================================

# ###isAdultBoolean = lambda age : if age > 18: return "Adult" else: return "Minor"
# isAdultBoolean = lambda age : "Adult" if age > 18 else "Minor"      ## working like Ternary operator in other program

# def isAdult(age):
#     if age > 18:
#         return "Adult"
#     else:
#         return "Minor"
# ###====================================================================================

# isAdultString = lambda age : "Adult" if age > 18 else "Minor" if age > 10 else "super minor"      ## Ternary operator 
# def isAdult(age):
#     if age > 18:
#         return "Adult"
#     else:
#         if(age > 10):
#             return "Minor"
#         else:
#             return "Super Minor"

# print(isAdult(30))      #True

# print(isAdultBoolean(20))       #True
# print(isAdultString(5))


# ###===================================================

# print((lambda age : age > 18)(20))       # Inline lambda fucntion call
# ##print((lambda age : age > 18)(20,40))  #TypeError: <lambda>() takes 1 positional argument but 2 were given     # Inline lambda fucntion call

# ###====================================================================================
# age = 5
# print(age > 18)

# ###=============================================================

listNumber  = [[10,1], [5,64],[1,98],[9,10]]
listNumber.sort()
print(listNumber)   #[[1, 98], [5, 64], [9, 10], [10, 1]]


listNumber  = [[10,1], [5,64],[1,98],[9,10]]
listNumber.sort(key= lambda a : a[1])       ## sort by value of sencond index in each list item
print(listNumber)   #[[10, 1], [9, 10], [5, 64], [1, 98]]


listNumber  = [[10,1,45], [5,64, 11],[1,98, 10],[9,10,99]]
listNumber.sort(key= lambda a : a[2])     ## sort by value of sencond index in each list item
print(listNumber)   #[[1,98, 10], [5,64, 11], [10,1,45], [9,10,99]]

### Sort decending
listNumber  = [[10,1,45], [5,64, 11],[1,98, 10],[9,10,99]]
listNumber.sort(key= lambda temp : temp[2], reverse=True)     ## sort by value of sencond index in each list item
print(listNumber)   #[[1,98, 10], [5,64, 11], [10,1,45], [9,10,99]]

## Lambda function is only requried when we want to provid function as a argument or input to some other fucntion