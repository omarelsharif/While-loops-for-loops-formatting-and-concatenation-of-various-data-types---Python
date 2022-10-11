#Question 1


Acc = 0
Positives = 0
Negatives = 0
run  = 0
Total = 0
Num =0




while run ==0:
    Num = int(input("Enter an integer, the input ends if it is 0:"))
    if Num >0:
        Acc += 1
        Positives = Positives + 1

    if Num <  0:
        Negatives = Negatives + 1

        Acc += 1
    Total = Total + Num

    if Num == 0:
        run = 1
       
        
if Acc >=1:
        
    Avg = Total / Acc

#FORMAT AVG TO 2 DECIMALS

if Acc >= 1 and run ==1:
    print("The total is", Total)
    print("The average is", '{0:.2f}'.format(Avg))

if Acc ==0 and run==1:
    print("No numbers are entered except 0")
