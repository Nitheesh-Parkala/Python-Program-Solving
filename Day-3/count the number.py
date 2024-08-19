n=int(input("Enter a number "))
count=0
while(n!=0):
    n=n//10
    count+=1
print(count)

# using function.

def checkCount(n):
    count=0
    while(n!=0):
     n=n//10
     count+=1
    return count

n=int(input("Enter a number "))
c=checkCount(n)
print(c)

#using range...

def checkCount(n):
    count=0
    while(n!=0):
     n=n//10
     count+=1
    return count

sr=int(input("enter a start "))
er=int(input("enter a end "))

if sr>er:
   print("invalid input")
else:
  for i in range(sr,er+1):
      c=checkCount(i)
      print("Number of digits:", i,":",c) 


  