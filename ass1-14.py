p=float(input('Enter the pressure in Pa(N/m^2): '))
t=float(input('Enter the temperature in K: '))
m=float(input('Enter the mass of the gas in kg: '))
mw=float(input('Enter the Molar mass in g: '))
#n=format((float(m/float(mw))),'.3f')#pv=nrt=>v=(nrt/p), Redbarg gas constant,r=8.314 J.K^-1.mol^-1
r=8.314
v=format((float((m*r*t)/float(p*mw))),'.3f')
print('Volume of the gas in cubic meter(m^3) is= '+str(v)+' m^3.')
print('\n\n\t\tHere we use Ideal Gas Equation, pV=nRT where R=8.314 J.K^-1.mol^-1.')
print('\n\t\t------------------CHANCHAL Kr. Laha-----------MCA-1A--------------')

