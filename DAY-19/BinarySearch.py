l=[1,8,15,22,36,45,72]

start=0
end=len(l)-1
flag=-1

target=72

while start<=end:
   mid=(start+end)//2

   if target==l[mid]:
      flag=mid
      break
   
   if target<l[mid]:
      end=mid-1
   else:
      start=mid+1

print(flag)
   

      

        
         
      

