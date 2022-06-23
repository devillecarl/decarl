#MITx 6.00.1x pset1
import time # for timing
#Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the credit card company each month.
#The following variables contain values as described below:
#balance - the outstanding balance on the credit card
#annualInterestRate - annual interest rate as a decimal
#monthlyPaymentRate - minimum monthly payment rate as a decimal
#For each month, calculate statements on the monthly payment and remaining balance.
#At the end of 12 months, print out the remaining balance. Be sure to print out no more than two decimal digits of accuracy - so print
balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
month = 1
while month <= 12:
    unpaid_balance = balance - monthlyPaymentRate * balance
    balance = unpaid_balance + annualInterestRate / 12 * unpaid_balance
    month += 1
print("Remaining balance:", round(balance, 2))
#calculate the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months.
#We can use the same variables as above, but instead of using the monthlyPaymentRate, we need to use the minimum fixed monthly payment.
#The program should print out one line: the lowest monthly payment that will pay off all debt in under 1 year, for example:
#Lowest Payment: 180
#Assume that the interest is compounded monthly according to the balance at the end of the month (after the payment for that month is made)
#The monthly payment must be a multiple of $10.
starttime=time.time()
balance=999999
annualInterestRate=0.2
monthlyInterestRate=annualInterestRate/12
monthlyUnpaidBalance=balance
updatedBalanceEachMonth=monthlyUnpaidBalance+(monthlyInterestRate*monthlyUnpaidBalance)
monthlyPayment=10
count=0
while updatedBalanceEachMonth>0:
    monthlyPayment+=10
    updatedBalanceEachMonth=balance
    for month in range(12):
        monthlyUnpaidBalance=updatedBalanceEachMonth-monthlyPayment
        updatedBalanceEachMonth=monthlyUnpaidBalance+(monthlyInterestRate*monthlyUnpaidBalance)
    count+=1
print("Lowest Payment:",monthlyPayment)
print("Execution Time without bisection :",time.time()-starttime)
print("Number of loops it took me without bisection :",count)

#use bisection search to find the minimum monthly payment to pay the debt in under 1 year.
#Assume that the interest is compounded monthly according to the balance at the end of the month (after the payment for that month is made)
#no more multiples of 10
#find the smallest monthly payment to the cent
starttime=time.time()
balance=999999
annualInterestRate=0.18
monthlyInterestRate=annualInterestRate/12
monthlyUnpaidBalance=balance
updatedBalanceEachMonth=monthlyUnpaidBalance+(monthlyInterestRate*monthlyUnpaidBalance)
monthlyPayment=0
lowestPayment=0
highestPayment=balance
countbisection=0
while abs(updatedBalanceEachMonth)>0.01:
   monthlyPayment=(lowestPayment+highestPayment)/2
   updatedBalanceEachMonth=balance
   countbisection+=1
   for month in range(12):
       monthlyUnpaidBalance=updatedBalanceEachMonth-monthlyPayment
       updatedBalanceEachMonth=monthlyUnpaidBalance+(monthlyInterestRate*monthlyUnpaidBalance)
   if updatedBalanceEachMonth>0:
       lowestPayment=monthlyPayment
   else:
       highestPayment=monthlyPayment
print("Lowest Payment:",round(monthlyPayment,2))
print("Execution Time with bisection :",time.time()-starttime)
print("Number of loops it took me without bisection :",countbisection)
