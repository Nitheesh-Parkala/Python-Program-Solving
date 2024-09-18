mountainArr=[1,2,3,4,5,3,1]
start=1
#end: arr.length()-2
end=len(mountainArr)-2
peak=-1

while start<=end:
    mid=(start+end)//2
    #left=mountainArr.get(mid-1)
    left=mountainArr[mid-1]
    #center=mountainArr.get(mid)
    center=mountainArr[mid]
    #right=mountainArr.get(mid+1)
    right=mountainArr[mid+1]

    if left<center>right:
        peak=center
        break

    if left<center<right:
        start=mid+1

    elif left>center>right:
         end=mid-1
print(peak)

# Binary Search For ASC ordered list.
targetIndex=-1
target=5
start=0
end=peak

while start<=end:
    mid=(start+end)//2

    if target==mountainArr[mid]:
        targetIndex=mid
        break

    if target<mountainArr[mid]:
        end=mid-1
    else:
        start=mid+1
# Binary Search For DSC ordered list.
if targetIndex==-1:
   
   start=peak+1
   end=len(mountainArr)-1

while start<=end:
    mid=(start+end)//2

    if target==mountainArr[mid]:
        targetIndex=mid
        break

    if target<mountainArr[mid]:
        start=mid+1
    else:
        end=mid-1

print(targetIndex)