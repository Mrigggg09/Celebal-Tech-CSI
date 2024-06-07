n=int(input("Enter number of rows(size):"))

#Lower Triangular Pattern

print("Lower Triangular Pattern:")
for i in range(n):
    print('*'*(i+1))

#Upper Triangular Pattern

print("Upper Triangular Pattern:")
for i in range(n):
    print(' '*i,end="")
    print('*'*(n-i))

#Pyramid Pattern

print("Pyramid Pattern:")
for i in range(n):
    print(end=" "*(n-i-1))
    print('*'*((i*2)+1))
