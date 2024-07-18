def gdc(num1,num2):
    gdc=1
    for i in range(1,min(num1,num2)):
        if num1 % i == 0 | num2 % i == 0:
            gdc=i
    print("the gdc is:",gdc)

num1=int(input("enter the value of num1:"))
num2=int(input("enter the value of num2:"))

gdc(num1,num2)
