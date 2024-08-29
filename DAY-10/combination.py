# n=3
# i | j    | noc
# 1 | 1-1  | 1
# 2 | 1-2  | 2
# 3 | 1-3  | 3
# 4 | 1-2  | 2
# 5 | 1-1  | 1

n=int(input("Enter a Number: "))
noc=0
for i in range(1,(n*2)): #Here actually (n*2)-1 but pvm internally decrement the loop.so we no need to put -1 after (n*2).
    if(i<=n):
        noc=noc+1
    else:
        noc=noc-1
    for j in range(1,noc+1):
        print("*",end=" ")
    print()