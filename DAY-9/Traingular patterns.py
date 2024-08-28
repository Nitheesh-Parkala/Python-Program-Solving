#7.
# (1-n) (1-i)
# i | j
# 1 | 1-4
# 2 | 1-4
# 3 | 1-4
# 4 | 1-4
n=int(input("Enter a Number: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
print("==============================")

#8. decrementing loops.
n=int(input("Enter a Number: "))
for i in range(1,n+1):
    for j in range(n,i-1,-1): #means n=4 ,i=1-1, if n>i then it should print * after that step -1 means n will become n=3. it will keep on going until n will become zero.
        print("*",end=" ")
    print()
