l=float(input('Enter the length of the thread of the simple pendulum in meter,length= '))
t=float(input('Enter the Time period of simple pendulum in second,T= '))
g=format(float(4*3.14*3.14*l)/(t*t),'.3f')
print('Therefore Gravitational Acceleraiton,g in m/s^2 is= '+str(g)+' m/s^2.')
