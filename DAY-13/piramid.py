# n=4
# i | j
# 1 | 1-1
# 2 | 1-3
# 3 | 1-5
# 4 | 1-7

n=int(input("Enter a Val: "))
odd=1

for i in range(1,n+1):
    for k in range(n,i-1,-1):
        print(" ",end=" ")
    for j in range(1,odd+1):
        print("*",end=" ")
    print()
    odd=odd+2
