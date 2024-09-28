def filtration(str):
    newstr=""

    for i in range(len(str)):
        #uppercase
        if "A"<=str[i]<="Z":
            newstr=newstr+chr(ord(str[i])+32)

        elif "a"<=str[i]<="z" or "0"<=str[i]<="9":
            newstr+=str[i]

    return newstr

def checkPalindrome(str):
    str=filtration(str)
    i,j=0,len(str)-1

    while i<=j:
        if str[i]!=str[j]:
            return False
        i+=1
        j-=1
    return True
    
str=input("Enter a String: ")
flag= checkPalindrome(str)

if flag:
    print("Is Palindrome")
else:
    print("Not Palindrome")


