l1=[10,8,7,6]
l2=[87,85,3,2,1,-1]

res=[]
i,j=0,0
while(i<len(l1) and j<len(l2)):
    if (l1[i]>l2[j]):
        res.append(l1[i])
        i+=1
    else:
        res.append(l2[j])
        j+=1
while(i<len(l1)):
    res.append(l1[i])
    i+=1
while(j<len(l2)):
    res.append(l2[j])
    j+=1
print(res)

print("========== Using for Loop =========")

l1 = [10, 8, 7, 6]
l2 = [87, 85, 3, 2, 1, -1]

res = []
i, j = 0, 0

# Merging both lists with for loop until one list is exhausted
for _ in range(len(l1) + len(l2)):
    # Break if one list is exhausted
    if i >= len(l1) or j >= len(l2):
        break

    # Compare elements from both lists and append the larger one
    if l1[i] > l2[j]:
        res.append(l1[i])
        i += 1
    else:
        res.append(l2[j])
        j += 1

# Append the remaining elements from l1 if any
for k in range(i, len(l1)):
    res.append(l1[k])

# Append the remaining elements from l2 if any
for k in range(j, len(l2)):
    res.append(l2[k])

print(res)


