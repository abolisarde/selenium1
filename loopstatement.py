
# # iList = [10, 30, 90, 20, 60]
# # for temp in iList:
# #      print(temp)
    
# ##1. Need to stop loop if element is 90
# ### Break will be breaking only loop not a program
# # iList = [10, 30, 90, 20, 60]
# # for temp in iList:
# #     if(temp == 90):
# #         break  ## Complete loop will be stopped and rest program after loop will continue to execute 
# #                ## loop Body after break will not execute  
# #     print(temp)
# # print("After complete loop")

# ###==================================================================
# ## we need to filter out even numbers
# # iList = [10, 31, 90, 267, 61]
# # for temp in iList:
# #     if(temp % 2 == 0):
# #         print(temp)
        
# # print("After complete loop")


# ###==================================================================
# ## we need to filter out odd numbers
# iList = [10, 31, 90, 267, 61]
# for temp in iList:
#     if(temp % 2 != 0):      #if(not temp % 2 == 0)
#         print(temp)
        
# print("After complete loop")

# ###==================================================================
# ## we need print odd numbers
iList = [10, 31, 90, 267, 61]
for temp in iList:
    if(temp % 2 == 0):
        continue       
                        
    print(temp)
        
print("After complete loop")

# ##==================================================

# iList = [10, 31, 90, 267, 61]
# for temp in iList:
#     if(temp % 2 == 0):
#         pass        ##     
#     print(temp)
        
# print("After complete loop")
