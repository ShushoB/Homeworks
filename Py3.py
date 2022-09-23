n = int(input("Enter the element number in Fibonacci Series: ")) 
def Fibonacci(n): 
    if n<0: 
        print("Try a natural number next time") 
    elif n==0: 
        return (0) 
    elif n==1 or n==2: 
        return (1)
    else: 
        return (Fibonacci(n-1)+Fibonacci(n-2)) 
print(n , "th Fibonacci number is: " , Fibonacci(n)) 
