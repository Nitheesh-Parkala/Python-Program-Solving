# n=int(input("enter a number "))
# temp=n
# rev=0
# while(n!=0):
#     rem=n%10
#     rev=(rev*10)+rem
#     n=n//10
# if(temp==rev):
#     print("the number is a palindrome")
# else:
#     print("the number is not a palindrome")


def reverseNumber(n):
    rev=0
    while(n!=0):
        rem=n%10
        rev=(rev*10)+rem
        n=n//10
    return rev
n=int(input("enter a number "))
temp=n
reverse=reverseNumber(n)
if(reverse==temp):
    print("The number is palindrome")
else:
    print("The Number is Not palindrome")
