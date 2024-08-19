def checkFizzBuzz(n):
    if(n%3==0 and n%5==0):
        return "fizzBuzz"
    elif(n%3==0):
        return "fizz"
    elif(n%5==0):
        return "buzz"
    else:
        return "Non fizz or buzz"

sr=int(input("Enter a Value1 "))
er=int(input("Enter a Value2 "))

if(sr>er):
    print("input is invalid")
else:
   print("FizzBuzz:")
   for i in range(sr,er+1):
       if (checkFizzBuzz(i))=="fizzBuzz":
           print(i,end=" ")

   print("\nFizz:")
   for i in range(sr,er+1):
       if(checkFizzBuzz(i))=="fizz":
        print(i,end=" ")

   print("\nBuzz:")
   for i in range(sr,er+1):
       if(checkFizzBuzz(i))=="buzz":
        print(i,end=" ")

   print("\nnon fizz or buzz:")
   for i in range(sr,er+1):
       if(checkFizzBuzz(i))=="Non fizz or buzz":
        print(i,end=" ")
    