n=int(input("Enter a Number: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")

    for j in range(2*(n-i)):
        print(" ",end=" ")

    for j in range(1,i+1):
        print("*",end=" ")
    print()


for i in range(1,n+1):
    for j in range(n-i+1):
        print("*",end=" ")

    for j in range(2*(i-1)):
        print(" ",end=" ")

    for j in range(n-i+1):
        print("*",end=" ")
    print()

