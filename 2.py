#distance between two points
x1=int(input('Enter x1='))
y1=int(input('Enter y1='))
x2=int(input('Enter x2='))
y2=int(input('Enter y2='))
distance=(((x2-x1)**2)+((y2-y1)**2))**0.5
print('Distance betwwen two points'+'('+str(x1)+','+str(y1)+')'+'and'+'('+str(x2)+','+str(y2)+')'+'is'+str(distance))
