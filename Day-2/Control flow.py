# n=int(input("enter a num: "))

# if(n%2==0):
#     print(n,"is the even number")
# else:
#     print(n,"is the odd number")
# print("ENd...")

# print("===================================")

# status=input("Check weather the person is ")
# tick= input("Enter a tick")
# if status=="online" and tick=="double tick ":
#      print("he is not seen msg...")

# elif status=="online" and tick=="blue tick":
#      print("Msg is seen")
# else:
#      print("he is offline")
# print("you  can call")

print("=====================================")

num=int(input("Enter a Number "))
if(num%2==0 and num<0):
    print("negative even num")

elif(num%2!=0 and num<0):
    print("Negative odd number")

elif(num%2==0 and num >0):
    print("Number is positive and even")

elif(num%2!=0 and num>0):
    print("Positive and odd")
else:
    print("Number is neutral")

