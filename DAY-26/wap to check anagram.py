def filtration(s1):
    nstr=""

    for i in range(len(s1)):
        if "A"<=s1[i]<="Z":
            nstr+=chr(ord(s1[i])+32)
        elif "a"<=s1[i]<="z":
            nstr+=s1[i]
    return nstr

def checkAnagram(s1,s2):
    s1=filtration(s1)
    s2=filtration(s2)
    if len(s1)!=len(s2):
        return False
    else:
        ascii=[0]*26
        for i in range(len(s1)):
          ascii[ord(s1[i])-97]+=1
          ascii[ord(s2[i])-97]-=1

        for i in ascii:
            if i!=0:
                return False
        return True

s1=input("Enter a String1: ")
s2=input("Enter a String2: ")
flag=checkAnagram(s1,s2)
if flag:
    print("Anagram")
else:
    print("Not anagram")