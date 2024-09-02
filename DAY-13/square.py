n=int(input("Enter a Number: "))

for i in range(n,0,-1):
    for j in range(n,0,-1):
        if j < i:
            print(j,end=" ")
        else:
            print(i,end=" ")
    print()


