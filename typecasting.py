# 10+10   # 20
#print(10+10)     # 20
#print ("10"+"10")       #1010
#print("10"+10)       ##TypeError: can only concatenate str (not "int") to str

###----------------------------------------------------------------------------------------------------------------

#aValue=10
#bValue=20
#print(aValue+bValue)             #30

###----------------------------------------------------------------------------------------------------------------

#aValue=10
#bValue="20"
#print(aValue+bValue)      #TypeError: unsupported operand type(s) for +: 'int' and 'str'


###----------------------------------------------------------------------------------------------------------------

#aValue=10
#bValue="20"
#convertebValue=int(bValue)    #int() is function which takes input and convert and provide value in integer

#print(aValue+convertbValue)   #30


###----------------------------------------------------------------------------------------------------------------

#aValue=10
#bValue="20"
#converteaValue=str(aValue)   

#print(converteaValue + bValue)   #1020

#print(converteaValue +" " bValue)   #1020


##------------------------------------------------------------------

#aValue=10.5
#bValue=20
#converteaValue=str(aValue)   

#print(aValue + bValue)         #30.5


######=====================================

#aValue=10.5
#bValue="20"
#converteaValue=str(aValue)   

#print(aValue + bValue)         #30.5


######=====================================

#aValue=10.5
#bValue=20
   

#print(int(aValue) + bValue)         #30



######=====================================

#aValue=10.5
#bValue=20
#result=aValue +float(bValue) 

#print (result)       #30.5


###-------------------------------------------------------------------------------------
##interview  **** 

#print(int(aValue) + bValue)      # ValueError: invalid literal for int() with base 10: '10.5'

##================================================================

# aValue = "10fsd"  #str  ## 

# print(int(aValue))      # ValueError: invalid literal for int() with base 10: '10fsd'

# ##==================================================================

# aValue = "True"  #str  ## 

# print(bool(aValue))      # True
# print(type(bool(aValue))) ##"<class 'bool'>"
##==================================================================

# aValue = "False"  #str  ## 

# print(bool(aValue))      # True
# print(type(bool(aValue)))  ##"<class 'bool'>"
# ##==================================================================
# ### bool returns False only for "" empty string and for anything else it will return True
# aValue = ""  #str  ## 

# print(bool(aValue))      # False
# print(type(bool(aValue)))  ##"<class 'bool'>"
# ##==================================================================

# ### eval()


#aValue = "False"  #str  ## 

#print(eval(aValue))      # False
#print(type(eval(aValue)))  ##"<class 'bool'>"


#print(type(eval(aValue)))  ##"<class 'bool'>"


# aValue = "sdfs"  #str  ## 

# print(eval(aValue))      
#print(type(eval(aValue)))          #



aValue = "10.4"  #str  ## 

print(eval(aValue))      # False
print(type(eval(aValue)))  ##"<class 'bool'>"









