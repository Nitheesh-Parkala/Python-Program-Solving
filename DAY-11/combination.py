# n=4
# i | j    | noc
# 1 | 1-4  | 4
# 2 | 1-3  | 3
# 3 | 1-2  | 2
# 4 | 1-1  | 1
# 5 | 1-2  | 2
# 6 | 1-3  | 3
# 7 | 1-4  | 4

n=int(input("Enter a Number: "))
noc=n
for i in range(1,(n*2)): #Here actually (n*2)-1 but pvm internally decrement the loop.so we no need to put -1 after (n*2).
    for j in range(1,noc+1):
        print("*",end=" ")
    print()
    if(i< n):
        noc=noc-1
    else:
        noc=noc+1
# O/p:
# * * * * 
# * * *
# * *
# *
# * *
# * * *
# * * * *
print("================================================")

# n=3
# i | j    | noc | space
# 1 | 1-1  | 1   | 3>1
# 2 | 1-2  | 2   | 3>2
# 3 | 1-3  | 3   | 3>3
# 4 | 1-2  | 2   | 3>2
# 5 | 1-1  | 1   | 3>1

n=int(input("Enter a Number: "))
noc=1
for i in range(1,(n*2)):
    # for k in range(n,noc,-1):
    for k in range(noc,n):
        print(" ",end=" ")
    
    for j in range(1,noc+1):
        print("*",end=" ")
    print()
    if(i<n):
        noc=noc+1
    else:
        noc=noc-1
# O/P:
#     * 
#   * *
# * * *
#   * *
#     *