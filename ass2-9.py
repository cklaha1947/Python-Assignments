a=float(input('Enter First angle='))
b=float(input('Enter Second angle='))
c=float(input('Enter Third angle='))
if (a+b+c==180):
    if (a==60 and b==60 and c==60):
        print('This is An Equiangular Triangle and also Acute angle Triangle.')
    elif (a==90 or b==90 or c==90):
        print('This is Rightangle Triangle.')
    elif (a<90 and b<90 and c<90  ):
        print('This is Acute angle Triangle.')
    elif ((a>90 and a<180) or (b>90 and b<180) or (c>90 and c<180)):
        print('This is Obtuse angle Triangle.')
else:
    print('This is an Invalid Triangle.')


    
        
        
