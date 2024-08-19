def reverseNumber(n):
    temp=n
    rev=0
    while(n!=0):
        rem=n%10
        rev=(rev*10)+rem
        n=n//10
    return rev==temp
 
sr=int(input("Enter a number1 "))
er=int(input("Enter a number2 "))

if(sr>er):
    print("The is invalid")
else:
    print("\nPalindrome:")
    for i in range(sr,er+1):
     if reverseNumber(i):
        print(i,end=" ")

    print("\nnonPalindrome:")
    for i in range(sr,er+1):
     if reverseNumber(i)==False:
        print(i,end=" ")









    
#     print("The number is palindrome")
# else:
#     print("The Number is Not palindrome")