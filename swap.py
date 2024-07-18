# Write a program to swap the values of two variables without using temporary variable.

print('swapping numbers')
#with temp
def swaptemp(x,y):
    print("value of x before swap:",x)
    print("value of y before swap:",y)
    temp=x
    x=y
    y=temp
    print("value of x after swap:",x)
    print("value of y after swap:",y)

#without temp
def swap(x,y):
    x,y=y,x
    print("\nvalue of x after swap:",x)
    print("value of y after swap:",y)

x=int(input("Enter the value of x:"))
y=int(input("Enter the value of y:"))
swaptemp(x,y)
swap(x,y)