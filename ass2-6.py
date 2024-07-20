num=int(input('Enter 1 for {Pounds to INR.}....Enter 2 for {Dollar to INR.}....Enter 3 for {Euro to INR.} = '))


if (num==1 or num==2 or num==3):
    print('-------------THANK YOU-----------------\n ----------------You entered '+str(num)+'-------------------')
else:
    print('-------------------UPPS !!!!!!---------------------\n--------------SORRY----A WRONG DIGIT IS ENTERED \n -----------------PLEASE ENTER A CORRECT DIGIT-------------------------')
    
if (num==1):
    pound=float(input('For Pounds to INR. Currency conversion, Please Enter the amount in Pounds ='))
    print('\n\n\n IMPORTANT INFORMATION: 1 Pound = 102.17 Rs. (INR)**** ')
    inr=pound*102.17
    print('\n\n\n\t\t\t\t'+str(pound)+'pound = '+str(inr)+'Rs.(INR.)')
elif (num==2):
    doll=float(input('For Doller to INR. Currency conversion, Please Enter the amount in Doller ='))
    print('\n\n\n IMPORTANT INFORMATION: 1 Doller = 83.25 Rs. (INR)**** ')
    inr=doll*83.25
    print('\n\n\n\t\t\t\t'+str(doll)+'Doller = '+str(inr)+'Rs.(INR.)')
elif (num==3):
    euro=float(input('For Euro to INR. Currency conversion, Please Enter the amount in Euro ='))
    print('\n\n\n IMPORTANT INFORMATION: 1 Euro = 89.07 Rs. (INR)**** ')
    inr=euro*89.07
    print('\n\n\n\t\t\t\t'+str(euro)+'Euro = '+str(inr)+'Rs.(INR.)')
    
