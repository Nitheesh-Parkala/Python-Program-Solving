n=int(input("Enter a Number: "))
count1=1

for i in range(1,n+1):
    for j in range(1,i+1):
        if i%2!=0:
            print(count1,end=" ")
            count2=count1
        else:
            print(count2,end=" ")
            count2-=1
        count1+=1
    print()
    count2=count2+i+1