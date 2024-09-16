def maximum(l):
   max=-21467438
   maxIndex=-1
   for i in range(len(l)):
     if max<l[i]:
         max=l[i] 
         maxIndex=i 
   return max, maxIndex

l=[5,8,55,55,79,26,34,99,85]


ele,index=maximum(l)
       

print("The Max Ele of list ele:",ele,"index:",index)

