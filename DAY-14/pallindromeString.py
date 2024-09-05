str=input("Enter a String: ")
newStr=""

for i in str:
    newStr=i+newStr

if(str==newStr):
    print("This string is Palindrome")
else:
    print("This is Not Palindrome")