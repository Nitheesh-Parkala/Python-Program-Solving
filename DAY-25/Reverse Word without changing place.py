str="MY Name Is Nitheesh Prabhu"
word=""
newStr=""
for char in str:
    if char!=" ":
       word=char+word
    else:
        newStr+=word+" "
        word=""
newStr=newStr+word
print(newStr)
