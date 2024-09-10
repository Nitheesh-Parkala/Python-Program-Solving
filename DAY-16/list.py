l1=[]
l1.append(25)
l1.append(100)
l1[ 1]=300

l1.insert(0,400)
print(l1)

l2=[]
l2.insert(10,1000)

l1.extend(l2)
print(l1)

l1.append(l2)
print(l1)

l1.insert(2,l2)
print(l1)

l1.extend(34)   #It will get error 
print(l1)

