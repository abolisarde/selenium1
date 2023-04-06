
aTemp = [10, 30,4,6,3, 9]

var = [20, 60, 8, 12, 6, 18]  # element * 2

result = []
for item in aTemp:
    result.append(item * 2)

print(result)       ##[20, 60, 8, 12, 6, 18]

##==================================================================
aTemp = [10, 30,4,6,3, 9]

result = list(map(lambda item : item * 2, aTemp ))
print(result)       ##[20, 60, 8, 12, 6, 18]

##==================================================================
aTemp = [10, 30,4,6,3, 9]

result = list(map(lambda item : item * item, aTemp ))
print(result)       ##[100, 900, 16, 36, 9, 81]


##==================================================================
aTemp = ['hello', "how",'what','when','where', 'whom']

result = list(map(lambda item : item.upper(), aTemp ))
print(result)       ##[20, 60, 8, 12, 6, 18]

a = "welcome"
a.split()     ## split each char in list

print(''.join(aTemp))       ## join each element from list 