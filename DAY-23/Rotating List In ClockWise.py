l=[1,2,3,4,5]

rot=3

n=len(l)

for i in range(rot):
    last_element=l.pop()

    l.insert(0,last_element)
print(l)