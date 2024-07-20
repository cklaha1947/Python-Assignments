num=int(input('Enter Number of calls= '))
if(num<=75):
    x=75
elif(num>75 and num<(75+75)):
    x=num*0.75
elif(num>(75+75) and num<(75+75+90)):
    x=num*0.65
elif(num>(75+75+90)):
    x=num*0.55
print('Monthly Bill of the Subscriber is= '+str(x)+'Rs.')
 
