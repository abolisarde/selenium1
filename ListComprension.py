
## mixture of map and filter without using lambda

h_letters = [ letter for letter in 'credence' ]
print( h_letters)

number_list = [ x for x in range(20) if x % 2 == 0]
print(number_list)

h_letters = [ letter.upper() for letter in 'credence' ]
print( h_letters)

number_list = [ x * x for x in range(20) if x % 2 == 0]     ## for > map (expresion ) > filter (if)
print(number_list)