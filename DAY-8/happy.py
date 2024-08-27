# def checkHappy(n):
#     if n==1:
#         return True
#     elif n==4:
#         return False
#     sum=0
#     while(n!=0):
#         base=n%10
#         sum=sum+(base**2)
#         n=n//10
#     return checkHappy(sum)

# n=int(input("Enter a Number: "))
# falg=checkHappy(n)

# if falg:
#     print("Happy Number")
# else:
#     print("Not a Happy Number")


def checkHappy(i):
    if i==1:
        return True
    elif i==4:
        return False
    sum=0
    while(i!=0):
        base=i%10
        sum=sum+(base**2)
        i=i//10
    return checkHappy(sum)

sr=int(input("Enter a Num1 "))
er=int(input("Enter a Num2 "))

if sr>er:
    print("The Number is invalid")

else:
    print("Happy Number")
    for i in range(sr,er+1):
        flag=checkHappy(i)   
        if flag==True:
          print(i,end=" ")

    print("\nNot a Happy Number")
    for i in range(sr,er+1):
        flag=checkHappy(i)   
        if flag==False:
          print(i,end=" ")
   