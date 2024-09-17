def findMin(l):

    min=2147483648
    secmin=21474836458

    for i in range(len(l)):
        if(min>l[i]):
            secmin=min
            min=l[i]
        elif secmin>l[i] and min!=l[i]:
            secmin=l[i]

    return min,secmin


l=[1,2,3,-5,6,7,21,26]

ele,secmin=findMin(l)

print("The First Min:",ele,"The second Min:",secmin)