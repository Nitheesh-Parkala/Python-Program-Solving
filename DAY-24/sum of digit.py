def sumOfDigit(s):
    total=0
    for i in range(len(s)):
        data=s[i]
        intger=ord(data)
        if 65<=intger<=122:
            total+=intger
    return total

s1 = "Aa"
res = sumOfDigit(s1)
print("Sum of digits:", res)
