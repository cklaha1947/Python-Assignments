num=int(input('Enter total amount of money: '))
if(num>=2000):
    q=num//2000
    print('number of 2000Rs. notes is= '+str(q))
    r=num%2000
    if(r>=500 and r<2000):
        q1=r//500
        print('number of 500Rs. notes is= '+str(q1))
        r1=r%500
        if(r1>=200 and r1<500):
            q2=r1//200
            print('number of 200Rs. notes is= '+str(q2))
            r2=r1%200
            if(r2>=100 and r2<200):
                q3=r2//100
                print('number of 100Rs. notes is= '+str(q3))
elif(num>=500 and num<2000):
    q=num//500
    print('number of 500Rs. notes is= '+str(q))
    r=num%500
    if(r>=200 and r<500):
        q1=r//200
        print('number of 200Rs. notes is= '+str(q1))
        r1=r%200
        if(r1>=100 and r1<200):
            q2=r1//100
            print('number of 100Rs. notes is= '+str(q2))
elif(num>=200 and num<500):
    q=num//200
    print('number of 200Rs. notes is= '+str(q))
    r=num%200
    if(r>=100 and r<200):
        q1=r//100
        print('number of 100Rs. notes is= '+str(q1))
elif(num>=100 and num<200):
    q=num//100
    print('number of 100Rs. notes is= '+str(q))
print('\n\n\n\n\t\t\t********************HOPE YOU ENJOY IT*************************\n\n\t\t\t BY CHANCHAL Kr. LAHA----')
        
        
            
            
            
            
                
               
    
        
        
