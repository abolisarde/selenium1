# n=int(input("Enter no."))
# a=0
# b=1
# for i in range(n):
#     print(a)
#     c=a
#     a=b
#     b=c+a
#     # print(b)

string = "abhimanyu"
vowels = []
for i in string:
    if i in ['a', 'e', 'i', 'o', 'u']:
        vowels.append(i)
print(vowels)

str = "aboli"
vowels = 0
for i in str:
    if i in ['a', 'e', 'i', 'o', 'u']:
        vowels = vowels + 1
print(vowels)
