aTemp = {
            'id' : 1001,
            'favColor' : 'White',
            'institute' : 'Credence',
             1 : 'Monika',
             True : "India"
        }

# # print(aTemp.items())        #dict_items([('id', 1001), ('favColor', 'White'), ('institute', 'Credence'), (1, 'India')])

# # print(aTemp.keys())         #dict_keys(['id', 'favColor', 'institute', 1])


# # aTemp['favColors'] = 'black'    #if no key avaiable then create new
(aTemp.update({'favColor' : 'Black', 'newValue':10002 }))     #if no key avaiable then create new
# # # in case of update we can bulk update or add/insert
print(aTemp)


# print(aTemp['favColor'])        #White
print(aTemp.get('favColor'))
# print(aTemp.get('favSport'))    #None
# print(aTemp['favSport'])        #KeyError: 'favSport'
