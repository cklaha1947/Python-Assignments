p=float(input('Enter the principal amount in Rs.,P: '))
t=float(input('Enter the Time Period (in years.),(T): '))
r=float(input('Enter the Rate of Interest per annum(in %),r: '))
si=format(float((p*r*t)/100),'.3f')
print('Simple Interest is= '+str(si)+'%')
