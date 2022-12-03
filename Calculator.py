

sum = 0
while(True):
   
    num = input("Enter the price of item or press 'y' to quit\n")  
    if num != 'y':
        sum+=int(num)
    else:
        print(f"Total sum is: {sum}")    
        break
        
    
    