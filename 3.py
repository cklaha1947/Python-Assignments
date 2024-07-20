#average of two numbers and their deviation
num1=int(input('Enter the first number='))
num2=int(input('Enter the second number='))
avg=(num1+num2)/2
dev1=avg-num1
dev2=num2-avg
print('average of two numbers'+str(num1)+'and'+str(num2)+'is'+str(avg))
print('First deviation is='+str(dev1))
print('Second deviation is='+str(dev2))
