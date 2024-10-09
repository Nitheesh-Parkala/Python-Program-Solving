s1=input("Enter a string1:")
s2=input("Enter a string2:")

if len(s1)>len(s2):
    flag=s1
else:
    flag=s2

i,j=0,0
while(i<len(s1) and j<len(s2)):
    if(s1[i]>s2[j]):
        flag="s1"
        break
    elif(s2[j]>s1[i]):
        flag="s2"
        break
    else:
        i+=1
        j+=1
        
if i==len(s1) and j==len(s2):
    flag="equal"
elif i<len(s1):
    flag="s1"
elif j<len(s2):
    flag="s2"
        
if flag=="s1":
    print("s1 is Greater")
elif flag=="s2":
    print("S2 is greater")
else:
    print("Equal")