l1=[8,7,6,5,4,3,2]

flag="asc"
if l1[0]>l1[len(l1)-1]:
   flag="desc"

start=0
end=len(l1)-1
flag=-1

target=3

while(start<=end):
    mid=(start+end)//2

    if target==l1[mid]:
        flag=mid
        break

    if flag=="asc":
       #Asc logic
       if target<l1[mid]:
          end=mid-1
       else:
          start=mid+1
    else:
       #Desc Logic
       if target<l1[mid]:
          start=mid+1
       else:
           end=mid-1
        
print(flag)




