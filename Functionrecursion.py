

# #### --------------------------------------------------------

# ## factorial of 5 = 5 * 4 * 3 * 2 * 1   
# ##   120

# counter = 5
# result = 1
# while(counter > 1):
#     result *= counter   ## result = result * counter
#     counter -= 1         ## counter = counter -1 
# print("Factorial of 5 : ", result)         # Factorial of 5 : 120

# ## ---------------------------------------------------------------

# ## Recursion

# def getfactorial():  # function signature
#     print("getfactorial body")
#     print("before recursio call")
#     getfactorial()      ## inside body self function call # recursion
#     print("after recursio call")

# getfactorial()
###--------------------------------------------------------------

# ## factorial of 5 = 5 * 4 * 3 * 2
##RecursionError: maximum recursion depth exceeded [Previous line repeated 996 more times]
def getFactorial(number : int):
    if number <= 1:      # number == 1 or number == 0
        return 1
    return number *  getFactorial(number - 1)


fact = getFactorial(5)
print("Factorial of 5 : ", fact)    #Factorial of 5 :  120

# 5 * getFactorial(5 - 1)
# 5 *  4 * getFactorial(4 - 1)      #getFactorial(3)
# 5 *  4 * 3 * getFactorial(3 - 1)  # #getFactorial(2)
# 5 *  4 * 3 * 2 * getFactorial(2 - 1) 
# 5 *  4 * 3 * 2 * 1
# 5 *  4 * 3 * 2 * 1 * 0 * getFactorial(0 - 1 )

# 