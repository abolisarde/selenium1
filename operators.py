
## Arithmatic operators
# print(10 + 5)       ## 
# print(10 - 5)       ## 
# print(10 * 5)       ## 
# print(10 / 5)       ## 

##----------------------------------------------

#a = 10
#b = 20

# result = a + b 
# print(result)


# a = a + b 
# print(a)

# a += b          ## 30
# print(a)

# ##==================================
#a = 10
#b = 20
#a -= b 
#print(a)        ## -10

# ##-------------------------------------------
#= 10
#b = 20
#a *= b 
#print(a)        ### 200
    

# ##-------------------------------------------
#a = 10
#b = 20
#a /= b 
#print(a)        ## 0.5

# ##-------------------------------------------

# a = 10 
# b = 20
# print("a == b : ", a == b)       #False  # always returns Boolean True or False
# ###print("a == b : "+ a == b)       #TypeError: can only concatenate str (not "int") to str

## =========================
# True => 1
# False => 0

##==================================================================

# a = True
# b = False 

# print("a != b : ", a != b)       #True  # always returns Boolean True or False

###===========================================================

## Logical Operators
## works with boolean

# a = True
# b = True 

# print("a and b : ", a and b)  # True
# print("a or b : ", a or b)  # True
# print(" a and not b : ", a and not b)  # False
# print("not a or not b : ", not a or not b)  # False

# ###-=======================================================

# print("a == b and a != b : ", a == b and a != b)  # False
# print("a or b : ", a or b)  # True
# print(" a and not b : ", a and not b)  # False
# print("not a or not b : ", not a or (not b))  # False

# ##--------------=========================================

## Interview 
#a=10
#b = 20  ## True

##print("a and b : ", True and True)  # 
#print("a and b : ", True or False)  # 


##a = 10  => any non zero value will be consider as True
#print("a and b : ", a and b)  # 20                      ##and =second value    or= first value
#print("a and b : ", a or b)  #  10

##===============================================

###Interview Assignment 
### VVVVVVVVVVIM
## Input 
# a = 30
# b = 40

## Swap two numbers using third variable

#c=a
#a=b
#b=c
#print ("value of a:",a)
#print("value of b:",b)



## Swap two numbers without using third variable

a = 30
b = 40

# print ("a:",a and b)
# print("b:",a or b)

a=a+b
b=a-b
a=a-b
print("a:",a)
print("b:",b)

##output 
#a = 40
#b = 30

