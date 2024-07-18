#Write a program for find factorial of a given number using iterative and recursive function. 

def factorial(x):
    fact = 1
    for i in range (1,n+1):
        fact = i * fact
    return fact

n = int(input("enter the value of n:"))
print("The factorial of",n,"using iterative function is",factorial(n))

def factorialr(n):
    if n==0 | n==1:
        return n
    else:
        return n*factorialr(n-1)
print("The factorial of",n,"using recursive function is",factorial(n))
