
#Question 2


print("Kilograms            Pounds")
for i in range(1,200):
    p = i * 2.2
    if i<=9:
    
        print(i, '{0:>25.1f}'.format(p))
    elif i<=99:
    
        print(i, '{0:>24.1f}'.format(p))
    
    else:
    
        print(i, '{0:>23.1f}'.format(p))
    

