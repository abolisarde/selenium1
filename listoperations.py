
listVariable = [1, 8, 9, 2, 10, 15]

# print(f"List before {listVariable}")    #List before [1, 8, 9, 2, 10, 15]
# output = listVariable.sort()
# print(f"List after sort {listVariable} and return output {output}")    #List after sort [1, 2, 8, 9, 10, 15] and return output None

# ## output will be all the time None, so no need to hold in variable and print 
# ####print(listVariable.sort())

print(f"List before {listVariable}")    #List before [1, 8, 9, 2, 10, 15]
output = listVariable.sort(reverse = True)
print(f"List after sort {listVariable}")    #List after sort [15, 10, 9, 8, 2, 1] and return output None
print(f"List after sort {listVariable} and return output {output}")    #List after sort [1, 2, 8, 9, 10, 15] and return output None

###========================================================================

## Reverse

# print(f"List before {listVariable}")    #List before [1, 8, 9, 2, 10, 15]
# listVariable.reverse()
# print(f"List after reverse {listVariable}")    #List after reverse [15, 10, 2, 9, 8, 1]
# # ###========================================================================

# ## Reverse

# # print(f"List before {listVariable}")    #List before [1, 8, 9, 2, 10, 15]
# # listVariable.reverse()
# # print(f"List after reverse {listVariable}")    #List after sort [1, 2, 8, 9, 10, 15] and return output None

# ### -------------------------------------------------
# listVariable = [1, 8, 9, 2, 10, 15]
# ##listVariable[5] = 100       # [1, 8, 9, 2, 10, 100]

# ## we can not assing or read value to index which is not currently in list
## instead we can use append funciton

# print(f"List before {listVariable}")    #List before [1, 8, 9, 2, 10, 15]
# listVariable[6] = 100           #IndexError: list assignment index out of range
# print(f"List after {listVariable}")    #List after sort [1, 2, 8, 9, 10, 15] and return output None

#======================================================================

# print(f"List before {listVariable}")    #List before [1, 8, 9, 2, 10, 15]
# listVariable.append(100)          #
# print(f"List after {listVariable}")    #List after [15, 10, 9, 8, 2, 1, 100]

[1, 8, 9, 2, 10, 15]
## Sorting => [1, 2, 8, 9, 10, 15]
## reverse => [15, 10, 2, 9, 8, 1]

### =============================================================
# listVariable = [1, 8, 9, 2, 10, 15]
# ###### listVariable[2] = 100       #[1, 8, 100, 2, 10, 15]     ## Value overwrite

# print(f"List before {listVariable}")    #List before [1, 8, 9, 2, 10, 15]
# listVariable.insert(2, 100)          
# print(f"List after {listVariable}")    #List after [1, 8, 100, 9, 2, 10, 15]

###===================================================================================

listVariable = [1, 8, 9, 2, 10, 15]

# print(f"List before {listVariable}")    #List before [1, 8, 9, 2, 10, 15]
# listVariable.pop(2)         ## will delete index 2 element    
# print(f"List after {listVariable}")    #List after [1, 8, 2, 10, 15]

###=====================================================

# print(f"List before {listVariable}")    #List before [1, 8, 9, 2, 10, 15]
# deleted = listVariable.pop()         ## will delete last element if no index given to pop    
# print(f"List after pop {listVariable} and deleted item {deleted}")    #List after pop [1, 8, 9, 2, 10] and deleted item 15


# ###=====================================================
# listVariable = [1, 8, 9, 2, 10, 15]

print(f"List before {listVariable}")    #List before [1, 8, 9, 2, 10, 15]
listVariable.remove(10)      ##pop(4)   
print(f"List after {listVariable}")    #List after  [1, 8, 9, 2, 15]

# ## Remove -  accept and remove value 
# ## pop - accept index and remove value from that index


color = ['Red', 'Green', 'blue', 'Purple','Orange', "Yellow", "Black"]
       #['Black', 'Blue', 'Green', 'Orange', 'Purple', 'Red', 'Yellow']
color.sort()
print(color)

color = ['Red', 'Green', 'Blue', None, 'Purple', 7, True, 'Orange', '10.5', "Yellow", "Black"]
color.reverse()
print(color)
