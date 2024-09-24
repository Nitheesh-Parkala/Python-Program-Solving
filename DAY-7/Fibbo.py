def checkFibbo(pos, n1, n2):
    if pos == 0:
        return
    print(n1)
    return checkFibbo(pos - 1, n2, n1 + n2)

pos = int(input("Enter the number of Fibonacci positions: "))
res=checkFibbo(pos, 0, 1)

#Fibonacci using Normal Function.

def checkFibbo(pos,n1,n2):
    for i in range(pos):
        print(n1)
        n1,n2=n2,n1+n2

pos=int(input("Enter a Number "))
checkFibbo(pos,0,1)

#Fibonacci without function.

pos=int(input("Enter a Number"))
n1=0
n2=1
for i in range(pos):
    print(n1)
    n1,n2=n2,n1+n2
