def checkEvenOdd(n):
    if(n%2==0):
     return True
    return False

start=int(input("enter a start "))
end=int(input("Enter the end "))

if start>end:
   print("invalid input")
else:
   
  for i in range(start,end+1):
   flag=checkEvenOdd(i)

   if(flag==True):
      print(i)
   
      
    

