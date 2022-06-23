#create a program to find the right amount of savings to save to reach a goal
total_cost = 4000000
portion_down_payment=0.25
downpayment=total_cost*portion_down_payment
annual_salary=float(input("Enter your annual salary: "))
current_savings = 0
r = 0.04
semi_annual_raise = 0.07
#find the best savings rate
while current_savings < downpayment:
    current_savings += annual_salary/12*r + current_savings*0.04/12
    r += 0.01
    if (current_savings*12)%6 == 0:
        annual_salary += annual_salary*semi_annual_raise


# total_cost=1000000.00
# portion_down_payment=0.25
# downpayment=total_cost*portion_down_payment
# current_savings=0
# r=0.04
# annual_salary=float(input("Enter your annual salary: "))
# semi_annual_raise=0.07


