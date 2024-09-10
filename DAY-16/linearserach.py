l1=[8,-2,3,6,77,89,45]
Target=77
flag=-1
for i in range(len(l1)):
    if (l1[i]==Target):
        flag=i
        break

if flag!=-1:
    print(Target,"is in index",flag)
else:
    print("Not found")

print("================This IS Using Function=============================")

def linearSearch(l1,Target):
  for i in range(len(l1)):
    if (l1[i]==Target):
        return i
  return -1

l1=[8,-2,3,6,77,89,45]
Target=77
res=linearSearch(l1,Target)


if res!=-1:
    print(Target,"is in index",res)
else:
    print("Not found")
