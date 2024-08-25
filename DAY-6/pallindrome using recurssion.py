def checkPalindrome(n,rev):
    if n==0:
        return rev
    rev=(rev*10)+(n%10)
    return checkPalindrome(n//10,rev)

num=int(input("Enter a Number "))
res=checkPalindrome(num,0)
if(num==res):
    print("number is palindrome")
else:
    print("Number is not palindrome")
