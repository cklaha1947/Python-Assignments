x=int(input('Enter [1 for Manager] or [2 for Officers] or [3 for Others] = '))    #x=designation,y=basic pay.
if(x==1):
    y=int(input('Enter Basic Pay= '))
    if(y<40000):
        fb=(y*12)/100
        if(fb<2500):
            fb1=2500
        else:
            fb1=fb
    elif(y>=40000):
        fb=(y*16)/100
        if(fb>7500):
            fb1=7500
        else:
            fb1=fb
    print('Amount of Festival Bonus is= '+str(fb1))
elif(x==2):
    y=int(input('Enter Basic Pay= '))
    if(y<20000):
        fb=(y*14)/100
        if(fb<2500):
            fb1=2500
        elif (fb>5000):
            fb1=5000
        else:
            fb1=fb
        print('Amount of Festival Bonus is= '+str(fb1))
    elif(y>=20000):
        print('More than 20000 basic pay is Not applicable for officers')
elif(x==3):
    y=int(input('Enter Basic Pay= '))
    fb=(y*8.9)/100
    fb1=fb
    print('Amount of Festival Bonus is= '+str(fb1))
elif(x!=1 and x!=2 and x!=3):
    print('\n\n\n\t\t\t\t\t---------------UPPS!!!!----------\n\n\n\t\t\t -------PLEASE ENTER THE CORRECT NUMBER 1/2/3-----------------')
        
       
