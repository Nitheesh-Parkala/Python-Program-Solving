l1=[5,8,10,15]
l2=[1,2,9,21,26,46]
res=[]
i,j=0,0
while (i<len(l1)and j<len(l2)):
        if(l1[i]<l2[j]):
            res.append(l1[i])
            i+=1
        else:
            res.append(l2[j])
            j+=1
while (i<len(l1)):
     res.append(l1[i])
     i+=1

while(j<len(l2)):
     res.append(l2[j])
     j+=1

print(res)