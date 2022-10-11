
#Question 5  


loanamount = float(input('Enter loan amount, for example 1200000.95: '))
years = int(input('Enter number of years as an integer, for example 5: '))



months = years * 12
interestrate = 5





print('Interest Rate','Monthly Payment','Total  Payment',sep='   ')


while interestrate <= 8:

    #Converting the annual interest to monthly interest
    variable = (interestrate/12)/100
    monthlypayment = loanamount * variable /(1-(1/  (1+variable)**months ))
    totalpayment = monthlypayment * months
    print('{0:.3f}%        {1:>8.2f}      {2:>15.2f}'.format(interestrate,monthlypayment,totalpayment))
    interestrate = interestrate + (1/8)
