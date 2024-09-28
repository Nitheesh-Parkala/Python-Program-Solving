str=input("Enter a String: ")
# str+=" "
newstr=""
word=""
for char in str:
    if char!=" ":
       word=word+char
    else:
        newstr=word+" "+newstr
        word=""
newstr=word+" "+newstr
print(newstr)