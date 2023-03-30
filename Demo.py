a=0
b=1
for i in range(0,5):
    c=a
    a=b
    b=c+b
    print(a)