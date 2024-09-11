l1 = [1, 2, 3]
l2 = [6, 9, 10]
res = []

i,j=0,0
for k in range(len(l1) + len(l2)):
        if k % 2 == 0:
            res.append(l1[i])
            i+=1
        else:
            res.append(l2[j])
            j+=1
print(res)


