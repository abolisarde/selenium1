aTupleVariable = [10, 20]       ## List type
aTupleVariable = (10, 20, 80, 30,15)       ## Tuple type

# print(aTupleVariable)       #(10, 20, 80, 30,15) 
# print(type(aTupleVariable)) #<class 'tuple'>

# print(len(aTupleVariable))      #5

# print(aTupleVariable[2])        ## 80

###aTupleVariable[2] = 100         ## tuple is immutable, we can not do assingment #TypeError: 'tuple' object does not support item assignment

###==================================================================

# aTupleVariable = 10, 20, 80, 30,15      ## Tuple type
# print(aTupleVariable)       #(10, 20, 80, 30,15) 
# print(type(aTupleVariable)) #<class 'tuple'>

## round bracket is optional however , comma is mandatory to create tuple

##=============================================================
aTupleVariable = (10)     ## Tuple type
print(aTupleVariable)       #(10, 20, 80, 30,15) 
print(type(aTupleVariable)) #<class 'int'>


##=============================================================
# aTupleVariable = (10,)     ## Tuple type
# print(aTupleVariable)       #(10,) 
# print(type(aTupleVariable)) #<class 'tuple'>

##=============================================================
# aTupleVariable = 10,     ## Tuple type
# print(aTupleVariable)       #(10,) 
# print(type(aTupleVariable)) #<class 'tuple'>
##=============================================================

aTupleVariable = ()     ## empty Tuple type
print(aTupleVariable)       #() 
print(type(aTupleVariable)) #<class 'tuple'>

aTupleVariable = tuple()     ## empty Tuple type
print(aTupleVariable)       #() 
print(type(aTupleVariable)) #<class 'tuple'>