l=[5,3,4,1,2]

#cycle
for i in range(0,len(l)-1):
    for j in range((i+1),0,-1):
        if l[j]<l[j-1]:
            l[j],l[j-1]=l[j-1],l[j]
print(l)

