
# # print("hello")
# # Print("Hello")      ## syntax error

##-------------------------------------------------------------

# a = [10, 60, 30, 50]
# print(a[1])     # 60

# ## Exception ## Runtime Exception
# print(a[4])     #   #IndexError: list index out of range

# # ## prog will stop execution if we dont handle these exceptions
# # ## to handle such exceptions we can use try except block
# print(a[0])
# print(a[2])

#==================================================================

# a = [10, 60, 30, 50]
# print(a[1])     # 60

# ## Exception ## Runtime Exception
# try:
#     print(a[0])    ## 10 
#     print(a[4])     #   #IndexError: list index out of range
#     print(a[0])     ## if exection occurs then next statement will not execute
#     print(a[1])     ## if exection occurs then next statement will not execute

# except:     ## catch the exception 
#     print("given index is not available in list")
#     ## we can write logic here to execute once exception occurs while executing try block
#     ## except block wil execute only if try has exception

# # ## prog will stop execution if we dont handle these exceptions
# # ## to handle such exceptions we can use try except block
# print(a[3])
# print(a[2])

#==================================================================

# a = [10, 60, 30, 50]
# print(a[1])     # 60

# ## Exception ## Runtime Exception
# try:
#     print(a[0])    ## 10 
#     print(a[4])     #   #IndexError: list index out of range
#     print(a[0])     ## if exection occurs then next statement will not execute
#     print(a[1])     ## if exection occurs then next statement will not execute

# ## Exception is base class for all exceptions
# except Exception as ex:     ## catch the exception 
#     print("Something is wrong :", ex)
#     ## we can write logic here to execute once exception occurs while executing try block
#     ## except block wil execute only if try has exception

# # ## prog will stop execution if we dont handle these exceptions
# # ## to handle such exceptions we can use try except block
# print(a[3])
# print(a[2])

# print("Excution completed")
# ##=======================================================================

# try:    
#     inputNumber = input("Enter number to divide to 100 : ")

#     result = 100 / int(inputNumber)
#     print("Result : ", result)
# except Exception as ex:
#     print("Error Occured : ", ex)



##=======================================================================

# try:    
#     inputNumber = input("Enter number to divide to 100 : ")
#     try:
#         result = 100 / int(inputNumber)
#         print("Result : ", result)
#     except:
#         print("Can not perform division operation")

# except ZeroDivisionError as z:
#     print("YOu can not enter 0 as input")
# except Exception as ex:
#     print("Error Occured : ", ex)


# ##=======================================================================

# try:    
#     inputNumber = input("Enter number to divide to 100 : ")
    
#     result = 100 / int(inputNumber)
#     print("Result : ", result)

# except ZeroDivisionError as z: #(Sorry, Dubara nahi karenge, if this excepttion doesnt match then next one will be checked)
#     print("YOu can not enter 0 as input: ",z)
# except ValueError as v:
#     print("Input value is invalid ", v)
# except Exception as ex:       #(chappal)
#     print("Error Occured : ", ex)



##=======================================================================

# try:    
#     inputNumber = input("Enter number to divide to 100 : ")
    
#     result = 100 / int(inputNumber)
#     print("Result : ", result)

# except Exception as ex:         ## (Chappal) all the time Exception block will excute
#     print("Error Occured : ", ex)
# except ZeroDivisionError as z:
#     print("YOu can not enter 0 as input", z)
# except ValueError as v:
#     print("Input value is invalid ", v)

#

#=======================================================================

try:    
    inputNumber = input("Enter number to divide to 100 : ")
    
    result = 100 / int(inputNumber)
    print("Result : ", result)

finally:        ## you can write only block however you can not write finally before except 
    print("Finally Excecuted.. all the time I excecute")


print("After try except finally")