def checkFibbo(pos, n1, n2):
    if pos == 0:
        return
    print(n1)
    return checkFibbo(pos - 1, n2, n1 + n2)

pos = int(input("Enter the number of Fibonacci positions: "))
res=checkFibbo(pos, 0, 1)

