def findMaxMin(l):
    min=2147483648
    max=-2147483648
    minIndex=-1
    maxIndex=-1


    for i in range(len(l)):
        if min>l[i]:
          min=l[i] 
          minIndex=i 
        if(max<l[i]):
            max=l[i]
            maxIndex=i
    return min,minIndex,max,maxIndex


l=[1,2,3,5,6,7,21,26]

ele,index,ele1,index1=findMaxMin(l)

print("The Min Ele of list ele:",ele,"index:",index)
print("The Max Ele of list ele:",ele1,"index:",index1)
