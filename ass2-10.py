a=float(input('Enter length of the first side= '))
b=float(input('Enter length of the second side= '))
c=float(input('Enter length of the third side= '))
if (a==b==c):
    print('This is an Equilateral Triangle.')
elif (a>b and a>c and (b+c)>a):
    if (b==c):
        print('This is an Isosceles Triangle.') 
    else:
        print('This is a Scalene Triangle.')
elif (a<b and a<c and (b+c)>a):
    if (b==c):
        print('This is an Isosceles Triangle.') 
    else:
        print('This is a Scalene Triangle.')
elif (b>a and b>c and (c+a)>b):
    if (a==c):
        print('This is an Isosceles Triangle.')
    else:
        print('This is a Scalene Triangle.')
elif (b<a and b<c and (c+a)>b):
    if (a==c):
        print('This is an Isosceles Triangle.')
    else:
        print('This is a Scalene Triangle.')
elif (c>a and c>b and (a+b)>c):
    if (b==a):
        print('This is an Isosceles Triangle.')
    else:
        print('This is a Scalene Triangle.')
elif (c<a and c<b and (a+b)>c):
    if (b==a):
        print('This is an Isosceles Triangle.')
    else:
        print('This is a Scalene Triangle.')

    
