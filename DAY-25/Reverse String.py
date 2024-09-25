#Normal Approach
str=input("Enter a String: ")
newStr=""

for i in range(len(str)):
    newStr=str[i]+newStr

print(newStr)

#Using Function
def reversString(str):
    newStr=""
    for i in range(len(str)):
        newStr=str[i]+newStr
    return newStr

str=input("Enter a String: ")
res=reversString(str)
print(res)

