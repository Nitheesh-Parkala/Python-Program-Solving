l1 = [1,8,9,10,11,12]
l2 = [6,8,10,12,13,26,21,7]
res = []

i,j=0,0
for k in range(len(l1) + len(l2)):
        if k % 2 == 0 and i<len(l1):
            res.append(l1[i])
            i+=1
        elif k%2!=0 and j<len(l2):
               res.append(l2[j])
               j+=1
        else:
              if(len(l1)<len(l2)):
                    res.append(l2[j])
                    j+=1
              else:
                    res.append(l1[i])
                    i+=1
print(res)  #Output: [1, 6, 8, 8, 9, 10, 10, 12, 11, 13, 12, 26, 21, 7]
