
import math
#Taking input from user
user_input =(input("Enter number"))
input_len = len(user_input)
user_number = int(user_input)
result = 0
num = user_number
while num > 0:
    rem = num%10

    result = int(math.pow(rem,input_len)) + result

    num = num//10 # round down and gives whole number


if result == user_number:
    print("Given number is armstrong",result)
else:
    print("Given number is not armstrong",result)    
