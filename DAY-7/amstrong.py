def countDig(n,count):
   if n==0:
     return count
   return countDig(n//10,count+1)

def checkASN(n,sum,temp,pow):
    if n==0:
        return temp==sum
    base=n%10
    sum+=base** pow
    return checkASN(n//10,sum,temp,pow)

n=int(input("Enter num: "))
pow=countDig(n,0)
flag=checkASN(n,0,n,pow)

if flag:
    print("ASN")
else:
    print("Not an ASN")