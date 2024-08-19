# n=int(input("enter a number "))
# rev=0
# if n<0:
#     n*=-1
# while(n!=0):
#1.extraction...........
#     rem=n%10
#2.alignment
#     rev=(rev*10)+rem
#3 remove the used digit.
#     n=n//10
# print("The reverse number is:",rev)

#Using function

def reverseNumber(n):
    rev=0
    while(n!=0):
        rem=n%10
        rev=(rev*10)+rem
        n=n//10
    return rev
n=int(input("enter a number "))
reverse=reverseNumber(n)
print("The reversed number is",reverse)

