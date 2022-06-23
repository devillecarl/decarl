print("Please think of a number between 0 and 100!")
low=0
high=100
ans=int((high+low)/2)
guessed=False
while not guessed: #while the difference between the guess and the answer is greater than epsilon
    print("Is your secret number " + str(ans) + "?")
    print("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    user_input=input()
    if user_input=='h':
        high=ans
    elif user_input=='l':
        low=ans
    elif user_input=='c':
        print("Game over. Your secret number was: " + str(ans))
        break
    else:
        print("Sorry, I did not understand your input.")
    ans=int((high+low)/2)
