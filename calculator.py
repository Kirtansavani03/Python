#Write a program to implement calculator.

def addition(x,y):
   return x+y
def subtraction(x,y):
   return x-y
def multiplication(x,y):
   return x*y
def division(x,y):
   return x/y

num1=int(input("Enter the value of num1:"))
num2=int(input("Enter the value of num2:"))
print("Enter the operation you want to perform")
print(" 1. for additon \n 2. for substraction \n 3. for multiplication \n 4. for division\n")
choice = int(input("Enter your choice: "))
if choice == 1:
   print("The result is:",addition(num1,num2))
elif choice == 2:
    print("The result is:",subtraction(num1,num2))
elif choice == 3:
    print("The result is:",multiplication(num1,num2))
elif choice == 4:
    print("The result is:",division(num1,num2))