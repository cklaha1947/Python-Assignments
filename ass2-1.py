sp=float(input('Enter the selling price(Rs.)='))
cp=float(input('Enter the cost price(Rs.)='))
if (sp>cp):
    profit=sp-cp
    print('profit of'+str(profit)+'Rs.')
elif (cp>sp):
    loss=cp-sp
    print('loss of'+str(loss)+'Rs.')
elif (sp==cp):
    print('Neither profit nor loss')
