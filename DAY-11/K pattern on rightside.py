n=int(input("Enter a Number: "))
noc=n
for i in range(1,(n*2)): #Here actually (n*2)-1 but pvm internally decrement the loop.so we no need to put -1 after (n*2).
    # for k in range(n,noc,-1):
    for k in range(noc,n):
        print(" ",end=" ")
        
    for j in range(1,noc+1):
        print("*",end=" ")
    print()
    if(i< n):
        noc=noc-1
    else:
        noc=noc+1

