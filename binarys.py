print("is your number a fraction 'f' or an integer 'i'?")
user_input=input()
while user_input!='f' and user_input!='i':
    print("Sorry, I did not understand your input.")
    user_input=input()
if user_input=='f':
    print("Please enter your fraction in the form 'numerator/denominator'")
    user_input=float(input())
    p=0
    while ((2**p)*user_input)%1!=0:
        print("Remainder ="+str((2**p)*user_input-int((2**p)*user_input)))
        p+=1
    num = int((2**p)*user_input)
    result =''
    if num==0:
        result='0'
    while num>0:
        result=str(num%2)+result
        num=num//2
    for i in range(p-len(result)):
        result='0'+result
    result = result[0:-p]+'.'+result[-p:]
    print('the binary representation of the decimal is: '+result)
elif user_input=='i':
    print("Please enter your integer")
    user_input=int(input())
    if user_input <0:
        isNegative=True
        user_input=abs(user_input)
    else:
        isNegative=False
    result=''
    if user_input==0:
        result='0'
    while user_input>0:
        result=str(user_input%2)+result
        user_input=user_input//2
    if isNegative:
        result='-'+result
    print("The binary notation of "+ str(user_input)+"is ", result)
else:
    print("Sorry, I did not understand your input.")