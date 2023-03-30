
# ## Function body will execute only if you call it as funcName() 
# def funcName():     ## Def => define # funcName => name of function, it can be anything
#     print("Hello Credence Global")      ## Function body# it can contain multiple statements.

# print("outside function")

# funcName()      ## Function call or trigger
# funcName()      ## Function call or trigger
# funcName()      ## Function call or trigger
# funcName()      ## Function call or trigger
# funcName()      ## Function call or trigger
# funcName()      ## Function call or trigger


###===================================================================

# def printInUpper(inputStr):
#     print(inputStr.upper())

# ## we need to provide mandatory input parameters to fucntion if not or skip few then it will give error
# ##printInUpper()  #TypeError: printInUpper() missing 1 required positional argument: 'inputStr'

# printInUpper("credence")        #CREDENCE
# printInUpper("hello")        #CREDENCE
# printInUpper("world")        #CREDENCE
# printInUpper("ct12")        #CREDENCE


###===================================================================
# ## function with one input parameter/argument
# def printInUpper(inputStr : str):       # providing parameter type is optional
#     print(inputStr.upper())

# ## we need to provide mandatory input parameters to fucntion if not or skip few then it will give error
# ##printInUpper()  #TypeError: printInUpper() missing 1 required positional argument: 'inputStr'

# printInUpper("credence")        #CREDENCE


### ===============================================================
## print() is inbuild function.. python developer created and we are reusing it 
## printInUpper() is user defined function.. we have created it and we are using.. if we want we can use in other files /folders


###-===========================================================================

# ## function with one optional input parameter/argument
# def printInUpper(inputStr : str = 'world'):       # providing parameter type is optional
#     print("Hello " + inputStr.upper())

# ## we need to provide mandatory input parameters to fucntion if not or skip few then it will give error
# ##printInUpper()  #TypeError: printInUpper() missing 1 required positional argument: 'inputStr'

# printInUpper("credence")        #Hello CREDENCE
# printInUpper()        # Hello WORLD



# aTemp = 'hello'
# result = aTemp.find('e')        #TypeError: find() takes at least 1 argument (0 given)
# print(result)


##============================================================

# # ## function with one optional input parameter/argument with return statement
# def printInUpper(inputStr : str = 'world'):       # providing parameter type is optional
#     return "Hello " + inputStr.upper()      ## return will provide result back where function is called
#     ### return statement will be last in function.. incase of you have other statements after return execution.. it will not execute
#     ## fanction can have multiple return statement. one return statement executed then it will stop/break function
# ##1
# result = printInUpper("credence")        #Hello CREDENCE
# print(result)

# ##2
# print(printInUpper("credence"))        # Hello WORLD

# result = printInUpper()        
# print(result)       # Hello WORLD

###===================================================

# def getInUpper(inputStr : str = 'world'):       # providing parameter type is optional
#     if (inputStr == 'credence'):
#         return "Hello " + inputStr.upper() 
#     else:
#         return "Invalid input"
    
# ##1
# result = getInUpper("credence")        #Hello CREDENCE
# print(result)

# ##1
# result = getInUpper("pune")        #Hello PUNE
# print(result)




# def getInUpper(inputStr : str = 'world'):       # providing parameter type is optional
#    return inputStr.upper() 


# strvalue = 'welcome'
# result= getInUpper(strvalue)
# if("WELCOME" == getInUpper(strvalue)):
#     print("Condition IS true")




# num = int(input("Enter the number :"))
# fac = 1
# for i in range (1,num + 1):
#  fac = fac * i
# print ("factorial of ",num,"is",fac)


# # num = int(input("Enter the number :"))

# # fac = 1
# # i=1
# # while i<=num:
# #     fac = fac * i
# # print ("factorial of ",num,"is",fac)




# import math
# a= math.factorial(5)
# print(a)


