str=input("Enter a String: ")
newStr=" "

for i in str:
    if i not in newStr:
        newStr=newStr+i
print(newStr)
