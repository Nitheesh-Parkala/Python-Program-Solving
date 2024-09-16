def minium(l):
   min=l[0]
   minIndex=-1
   for i in range(len(l)):
      if min>l[i]:
         min=l[i] 
         minIndex=i 
   return min,minIndex

l=[5,8,55,55,79,26,34,99,85]


ele,index=minium(l)
       

print("The Min Ele of list ele:",ele,"index:",index)