#Question 3


k = 1
p = 20

print("Kilograms            Pounds      |     Pounds             Kilograms")


while k <200:
    print ("{0:<3d}                  {1:<5.1f}       {2:<1s}     {3:<3d}                {4:<9.2f}".format(k,k*2.2,"|",p,p/2.2))
 

    k +=2
    p+=5
