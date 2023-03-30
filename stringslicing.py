
a = 10
b = 45.6
c= "welcome"

aValue  = "Welcome"

print(aValue)       #Welcome
print(aValue[0])       #w
# print(aValue[1])       #e
# print(aValue[3])       #c
# print(aValue[6])       #e

#  ###print(aValue[7])       #IndexError: string index out of range

print("Length of string : ", len(aValue))
print(aValue[len(aValue) - 1])       #e


#  print(aValue[0] + aValue[1] + aValue[2])       #Wel
#  print(aValue[0] + aValue[1] + aValue[2] +  aValue[3])  ## Wrong way write     #Welc

print(aValue[0:3])       #Wel
#  print(aValue[0:4])       #Welc

#  print(aValue[1:3])       #el

#  print(aValue[3:7])       #come
#  print(aValue[3:10])       #come


# # ## ------------------------------------
print(aValue[-1])       #e
print(aValue[-3])       # o
print(aValue[-6])       #e

#  print(aValue[-7:-1])       #Welcom
print(aValue[-7:0])  

#  print(aValue[-7:7])       #Welcome

#  print(aValue[-7:])       #Welcome


print(aValue[4:])       #ome

print(aValue[:4])       #Welc

print(aValue[:])       #Welc   ##print(aValue) 

print(aValue[0:7:1])       #Welcome
print(aValue[0:7:2])       #Wloe
print(aValue[0:7:3])       #wce
print(aValue[0:7:4])         #wo


