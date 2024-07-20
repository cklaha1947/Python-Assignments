therm=int(input('Enter the amount of gas used by the consumer(in therm unit): '))
if(therm<=125):
    x=therm*7.75
elif(therm>125 and therm<=250):
    x=((therm*9.75)*(1+(1.25/100)))
elif(therm>250):
    x=((therm*13)*(1+(2.5/100)))
total=x+23
print('Gas Bill for one month is ='+str(total)+'Rs.')

