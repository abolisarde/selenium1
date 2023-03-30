# aValue =  "welcome"

# # # print(aValue)       #Welcome
# # # print(len(aValue))          #7

# # # print("endswith('Come') : ", aValue.endswith("Come"))      #False capital c
# # # print(aValue.endswith("come"))      #True

# # # print(aValue.endswith("com"))      #False
# # # print(aValue.endswith("com"))      #False
# # # print(aValue.endswith("e"))      #True


# print(aValue.count("com"))      #1

# # # print(aValue.count("z"))      #0



# # # print(aValue.capitalize())      ##Welcome



# # aValue =  "welcome"

# # index = aValue.index('c')
# # print(index)        ##3

# # # # index = aValue.index('c',4,6)   # "om".index('c')
# # # # print(index)        ## ValueError: substring not found


# # index = aValue.index('c',3,6)   # "com".index('c')
# # print(index)        ## 3


# # # # index = aValue.index('e',3,6)   # "com".index('c')
# # # # print(index)        ## ValueError: substring not found



# # #### Interview question

# # aValue =  "welcome"

# # index = aValue.index('e',3,7)  
# # print(index)        ## ValueError: substring not found


# # firstEIndex = aValue.index('e')
# # secondIndex = aValue.index('e',firstEIndex + 1)
# # thirdIndex = aValue.index('e',secondIndex + 1)
# # print(f"First Index : {firstEIndex}, Second Index : {secondIndex}, Third Index : {thirdIndex}")



# # ## Assingment
# # ## I want 3rd index of given string

# # ## Find Function
# # ## Replace Function
# # ## lower
# # ## upper
# # ## isdigit

# # cValue="aboli"
# # print(cValue.lower())
# # print(cValue.upper())
# # newValue=cValue.replace("aboli","nboli")
# # print(f"old value {cValue}:new value after replace {newValue}")
# # print(cValue.isdigit())   ##isdigit() method returns True if all the characters are digits,otherwise False. 
# # print(cValue.count("l")) 
# # print(len(cValue))


# # newValue = aValue.replace("come", "done")

# # print(aValue)         #welcome

# # print(f"Old value {aValue} : new Value after replace {newValue}")


# # newValue = aValue.replace("come", "done").replace("e", '')

# # print(aValue)         #welcome

# # print(f"Old value {aValue} : new Value after replace {newValue}")


# # ### Google

# # # Gogle
# # bValue="Google"
# # newValue=bValue.replace("Google","Gogle")
# # #print(newValue)
# # print(f"old value {bValue}:new value after replace {newValue}")


# #######################============== last batch notes==================



# # aValue =  "welcome"

# # print(aValue)       #Welcome
# # print(len(aValue))          #7

# # print("endswith('Come') : ", aValue.endswith("Come"))      #False
# # print(aValue.endswith("come"))      #True

# # print(aValue.endswith("com"))      #False
# # print(aValue.endswith("com"))      #False
# # print(aValue.endswith("e"))      #True


# # print(aValue.count("e"))      #2
# # print(aValue.count("z"))      #0



# # print(aValue.capitalize())      ##Welcome



# aValue =  "welcome"

# index = aValue.index('c')
# print(index)        ##3

# # # index = aValue.index('c',4,6)   # "om".index('c')
# # # print(index)        ## ValueError: substring not found


# index = aValue.index('c',3,6)   # "com".index('c')
# print(index)        ## 3


# # # index = aValue.index('e',3,6)   # "com".index('c')
# # # print(index)        ## ValueError: substring not found



# #### Interview question

# aValue =  "welcome"
# findstr = 'e'

# index = aValue.index('e',3,7)  
# print(index)        ## ValueError: substring not found


# firstEIndex = aValue.index(findstr)
# secondIndex = aValue.index(findstr,firstEIndex + 1)
# thirdIndex = aValue.index(findstr,secondIndex + 1)

# print(f"First Index : {firstEIndex}, Second Index : {secondIndex}")


# ## Assingment
# ## I want 3rd index of given string

# ## Find Function
# ## Replace Function
# ## lower
# ## upper
# ## isdigit

# newValue = aValue.replace("come", "done")

# print(aValue)         #welcome

# print(f"Old value {aValue} : new Value after replace {newValue}")


# newValue = aValue.replace("come", "done").replace("e", '')

# print(aValue)         #welcome

# print(f"Old value {aValue} : new Value after replace {newValue}")


# ### Google

# # Gogle

aValue = "Google"
print(aValue.replace("oo","o"))

