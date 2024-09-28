s1="AAaABb0100"
ascii=[0]*256
i=0

for i in range(len(s1)):
   ascii[ord(s1[i])]+=1

for i in range(len(ascii)):
    if ascii[i]!=0:
        print(chr(i),"-->",ascii[i])

