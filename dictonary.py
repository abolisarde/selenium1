
# employeesList = [ [101,'Aarti','749386'],  
#               [102,'Amol','749386'],
#               [103,'Rahul','749386'],
#               [104,'Sumit','749386'],
#               [105,'Suraj','749386'],
#               [106,'Rahul','749386'],
#               [107,'Aarti','749386']
#             ]

# dictionaryVariable = {'key' : 'value', 'id': 1001}          
# print(dictionaryVariable)               #{'key': 'value', 'id': 1001}
# print(type(dictionaryVariable))         # <class 'dict'>
# print(len(dictionaryVariable))          # 2 

# ## Dictionary doesnt support index
# ## print(dictionaryVariable[1])        # KeyError: 1

# # print(dictionaryVariable['id'])        #1001



employeesDict = {101 : [101,'Aarti','749386'],  
                 102 : [102,'Amol','749386'],
                 103 : [103,'Rahul','749386'],
                 104 : [104,'Sumit','749386'],
                 105 : [105,'Suraj','749386'],
                 106 : [106,'Rahul','749386'],
                 107 : (107,'Aarti','749386'),
                 '108' : ['108','Shubham','749386']
           }
# # print(employeesDict[104])       ##[104, 'Sumit', '749386']

# # ##print(employeesDict[108])       ##KeyError: 108 
# # ## we need to provide exact key with exact data types

# # print(employeesDict['108'])       ## ['108','Shubham','749386']
# # print(employeesDict)

# employeesDict[107][1] = 'Pratiksha'
# print(employeesDict)

# employeesDict[107] = 'Pratiksha'
# print(employeesDict)

# employeesDict[106][1] = 'Pratiksha'
# print(employeesDict)

# employeesDict[106] = 'Pratiksha'
# print(employeesDict)

# employeesDict[106][1][4]= 'Pratiksha'        #TypeError: 'str' object does not support item assignment
# print(employeesDict)

# #####======================================================


# aTemp = {
#             'id' : 1001,
#             'favColor' : 'White',
#             'institute' : 'Credence',
#              '1' : 'Monika',
#               1 : 'Nitin',
#              True : "India"
#         }
# print(aTemp)        #{'id': 1001, 'favColor': 'White', 'institute': 'Credence', 1: 'India'}
# aTemp['favColor'] = 'Black'
# print(aTemp)        #{'id': 1001, 'favColor': 'Black', 'institute': 'Credence', 1: 'India'}

# print(aTemp['1'])     #Monika

'1' == '1'

