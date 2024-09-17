def findMax(l):

    max=-2147483648
    secmax=-21474836458

    for i in range(len(l)):
        if(max<l[i]):
            secmax=max
            max=l[i]
        elif secmax<l[i] and max!=l[i]:
            secmax=l[i]

    return max,secmax


l=[1,2,3,5,6,7,21,26]

ele,secmax=findMax(l)

print("The First Max:",ele, "The second Max:",secmax)