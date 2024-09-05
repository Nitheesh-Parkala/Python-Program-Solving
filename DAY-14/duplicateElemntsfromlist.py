list=["Nitheesh","Prabhu","Nitheesh"]
newList=[]

for i in list:
    if i not in newList:
        newList.append(i)

print(newList)