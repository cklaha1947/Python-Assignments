bp=float(input('Enter the basic pay= '))
da=float((97*bp)/float(100))
hra=float((57*bp)/float(100))
ma=150
epf=float((12*bp)/float(100))
pt=200
gp=(bp+da+hra+ma)-(epf+pt)
salary=gp-pt
print('Therefore net salary is= '+str(salary)+' Rs. .')
