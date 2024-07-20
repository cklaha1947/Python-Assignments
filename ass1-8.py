a=float(input('Enter the length of the base of the room,a= '))
b=float(input('Enter the breath of the base of the room,b= '))
h=float(input('Enter the height of the room,h= '))
p=float(input('Enter the cost of painting for 1 square meter.= '))
s4=2*(a+b)*h
s6=s4+(2*a*b)
c4=s4*p
c6=s6*p
print('\n\n\t--------------------------------------------------------------------------------------')
print('\tarea of four walls= '+str(s4)+' m^2 '+'and cost of its painting is= '+str(c4)+' Rs.')
print('\tarea of all walls= '+str(s6)+' m^2 '+'and cost of its painting is= '+str(c6)+' Rs.')


