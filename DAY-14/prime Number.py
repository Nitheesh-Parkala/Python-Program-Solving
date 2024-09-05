num=int(input("Enter a Number: "))
count=0
i=1

while(i<=num):
    if((num%i)==0):
        count=count+1
    i=i+1

if(count==2):
    print("Number is Prime")
else:
    print("Number is Not Prime")