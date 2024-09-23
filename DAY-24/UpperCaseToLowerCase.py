def checkLowerCase(s1):
    newStr=""
    for i in range(0,len(s1)):
       data=s1[i]
       intger=ord(data)
       if 65<=intger<=90:
          newIntger=intger+32
          newChar=chr(newIntger)
          newStr+=newChar
       else:
           newStr+=data
    return newStr

s1="ABcD"
res=checkLowerCase(s1)
print(res)