n=int(input("Enter a Number: "))
noc=1
nor=7
for i in range(1,(n*2)):
    for j in range(1,(n*2)):
       if j <= noc or j >= nor:
          print("*",end=" ")
       else:
          print(" ",end=" ")
    print()
    if(i<n):
        noc=noc+1
        nor=nor-1
    else:
        noc=noc-1
        nor+=1