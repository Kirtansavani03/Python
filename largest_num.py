print("largest number")
def largest(a,b,c):
    if(a>b and a>c):
        large=a
    elif(b>a and b>c):
        large=b
    else:
        large=c
    return large

a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
c=int(input("Enter the value of c:"))
print("Largest number is:",largest(a,b,c))
