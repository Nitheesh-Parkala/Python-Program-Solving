def reverse(i,str,newstr):
    if i==-1:
        return newstr
    newstr=newstr+str[i]
    return reverse(i-1,str,newstr)
str=input("Enter a String: ")
l=reverse(len(str)-1,str," ")
print(l)