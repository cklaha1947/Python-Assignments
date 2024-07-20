a=float(input('Enter the First side= '))
b=float(input('Enter the Second side= '))
c=float(input('Enter the Third side= '))
d=float(input('Enter the Fourth side= '))
e=float(input('Enter the angle in degree= '))
if(a==b and b==c and c==d and d==a and e==90):
    print('\n\n\t\tIt is a Square.')
elif(a==b and b==c and c==d and d==a and e!=90):
    print('\n\n\t\tIt is a rombosh')
elif(a==c and b==d and a!=b and e!=90):
    print('\n\n\t\tIt is a Parallelogram')
elif(a==c and b==d and a!=b and e==90):
    print('\n\n\t\tIt is a Rectangle.')
elif(a!=b and b!=c and c!=d and d!=a):
    print('\n\n\t\tIt is an Irregular quadrilateral.')
print('\n\t----------------------------CHANCHAL Kr. LAHA--------MCA 1A--------------------------------------------------')

