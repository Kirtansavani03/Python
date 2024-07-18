#Write a program which takes a sentence from user and calculates number of digits, letters, uppercase letters, lowercase letter and spaces in sentence. 
 
def countstring(string):
    lower=0
    upper=0
    digit=0
    space=0
    for i in string:
        if i.islower():
            lower=lower+1
        elif i.isupper():
            upper=upper+1
        elif i.isdigit():
            digit=digit+1
        elif i.isspace():
            space=space+1
    print("Numbers of letters is:",lower+upper)       
    print("Numbers of lowercase letters is:",lower)
    print("Numbers of uppercase letters is:",upper)
    print("Numbers of digits is:",digit)
    print("Numbers of spaces is:",space)

string=input("Enter the string:")

countstring(string)