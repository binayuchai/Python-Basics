
def fiboIter(n):
    a = 0
    b = 1
    for i in range(1,n):
        c = a+b
        a = b
        b = c
    
    return c


def fibo(n):
    #condition
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
        
        
if __name__ == '__main__':
    n = int(input("Enter the nth term of fibonacci series"))
    print("using recursion : ")
    print(f"The value of {n} term in fibonnaci series is: ",fibo(n))
    print("using iteration : ")        
    print(f"The value of {n} term in fibonnaci series is: ",fiboIter(n))  
