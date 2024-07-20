x=int(input('Enter (1 for A-region) or (2 for B-region): '))        #x=region,y=sales,c=commission.
if(x==1):
    y=float(input('Enter sales in Rs.= '))
    if(y<10000):
        c=0
    elif(y>=10000 and y<16000):
        c=(y*6.5)/100
    elif(y>=16000 and y<35000):
        c=((y*8.5)/100)+1500
    elif(y>=35000):
        c=((y*11)/100)+4500
    print('Amount of commission for A is= '+str(c)+'Rs.')
elif(x==2):
    y=float(input('Enter sales in Rs.= '))
    if(y<15000):
        c=(y*6.5)/100
    elif(y>=15000 and y<25000):
        c=((y*8.5)/100)+1500
    elif(y>=25000):
        c=((y*11)/100)+4500
    print('Amount of commission for B is= '+str(c)+'Rs.')
elif(x!=1 and x!=2):
    print('\n\n\n\t\t\t\t\t---------------UPPS!!!!----------\n\n\n\t\t\t -------PLEASE ENTER THE CORRECT NUMBER 1/2-----------------')
