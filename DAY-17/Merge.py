l1=[1,2,3]
l2=[4,5,6]
l3=[6,7,8]
print(id(l1))

l1=l1+l2
print(id(l1))
print(l1)

l1.extend(l3)
print(id(l1))
print(l1)
