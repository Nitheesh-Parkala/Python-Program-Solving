l=[5,6,4,2,1]

for i in range(0,len(l)-1):
    for j in range((len(l)-1-i)):
        # Asc
        if l[j]>l[j+1]:
             l[j],l[j+1]=l[j+1],l[j]

print(l)

print("===============")

l=[5,6,4,2,1]

for i in range(0,len(l)-1):
    for j in range((len(l)-1-i)):
        # Dsc
        if l[j]<l[j+1]:
             l[j],l[j+1]=l[j+1],l[j]

print(l)