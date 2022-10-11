
#Question 7
import random


acc = 1 
count = 1



while count <=5:
    x = random.randint(100,999)
    digit1=x%10
    y=x//10
    digit2=y%10
    z=y//10
    digit3=z%10
    if digit1==digit2 and digit2==digit3:
        print("Lottery number", acc, "is", x)
        count+=1
        acc+=1
