### List 

# [] - Square bracket
# () - Round Bracket
# {} - curly bracket
# 
 
color = ['Red', 'Green', 'Blue', None, 'Purple', 7, True, 'Orange', '10.5', "Yellow", "Black"]
print(color)            #['Red', 'Green', 'Blue']
# print(type(color))      ## <class 'list'>


# print(color[1])         #Green

print(color[0:3])         #['Red', 'Green', 'Blue']
# print(color[0:4])         #['Red', 'Green', 'Blue', 'Purple']

color[3] = 'Pink'
print(color)            #['Red', 'Green', 'Blue', 'Pink', 'Purple', 7, True, 'Orange', '10.5', 'Yellow', 'Black']

aStrValue = "Welcome"

# # # aStrValue[3] = 'd'      #TypeError: 'str' object does not support item assignment
# # # print(aStrValue[3])     

### String is immutable (not changable/ we can not modify string) datatype,
## we can not change single or few element/item/character from string
## however we can replace whole string

###===================================================================

# temp = aStrValue.replace('c','d').replace('m','n')
# print(aStrValue)
# print(temp)

# aStrValue = "weldone sdf sdfs werwerpdsf eh2u3"       # we can replace whole string

## List is mutable datatype, we can change single or few item or element from list as well as whole list
## immutable => can not be changed or modified
## mutable => can be changed or modified


print(color[1][0])      #G


# # color[1][0] = 'P'       #TypeError: 'str' object does not support item assignment
# # print(color)

# aStrValue = 'welcome'
# aStrValue = 'weldone'
# temp = aStrValue.replace('d','c')       # temp = welcone # aStrValue = weldone
# aStrValue = aStrValue.replace('d','c')  #aStrValue = 'weldone'


""  ## empty string
" "  ## single space
"  "    # double space ## 2 times single space

# google

#replace 'oo' with 'o'
#replace 'o' with '' , 1
