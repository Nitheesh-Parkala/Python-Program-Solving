def reverse(n,rev):
    if n==0:
        return rev
    rev=(rev*10)+(n%10)
    return reverse(n//10,rev)

num=int(input("Enter a Number "))
res=reverse(num,0)
print(res)





