#create a while loop for bisection search of the square root of a number from user input
number=float(input('Enter a number: '))
epsilon=float(input('Enter a precision: '))
num_guesses=0
low=0
high=number
ans=(high+low)/2.0
