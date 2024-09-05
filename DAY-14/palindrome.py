n=int(input("Enter a Number: "))
num=n
rev=0
while(n!=0):
    rem=n%10
    rev=(rev*10)+rem
    n=n//10

if(num==rev):
    print("Number is Pallindrome")
else:
    print("Number is Not Palindrome")
