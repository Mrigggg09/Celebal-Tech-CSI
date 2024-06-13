#Addition
def add(a,b):
    return a+b

#Substraction
def sub(a,b):
    return a-b

#Multiplication
def mult(a,b):
    return a*b

#Division
def div(a,b):
    return a/b


print("Welcome to your Python Calculator.\n")

print("Operation details:\n1 - for addition\n2 - for substraction\n3 - for multiplication\n4 - for division\nAny other number get result and exit\n")

a=int(input("Enter number : "))
while(True):
    choice = int(input("Enter operation : "))

    if(choice==1):
        b=int(input("Enter number :"))
        a=add(a,b)
    elif(choice==2):
        b=int(input("Enter number :"))
        a=sub(a,b)
    elif(choice==3):
        b=int(input("Enter number :"))
        a=mult(a,b)
    elif(choice==4):
        b=int(input("Enter number :"))
        a=div(a,b)
    else:
        print(a)
        break




