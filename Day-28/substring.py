s=input("Enter a sting: ")
substr=[]

for i in range(len(s)):
    newstr=""
    for j in range(i,len(s)):
        newstr=newstr+s[j]   # newstr is used to carry forward the value.
        substr.append(newstr)
print(substr)

# USing Function:

def dispalySubstring(s,substr):
   for i in range(len(s)):
    newstr=""
    for j in range(i,len(s)):
        newstr=newstr+s[j]   # newstr is used to carry forward the value.
        substr.append(newstr)
   return substr

s=input("Enter a sting: ")
substr=[]
res=dispalySubstring(s,substr)
print(res)
