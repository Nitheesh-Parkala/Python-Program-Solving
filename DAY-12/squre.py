n=int(input("Enter a Number: "))

for i in range(1,n+1):
    for j in range(1,n+1):
        if i < j:
            print(j,end=" ")
        else:
            print(i,end=" ")
    print()