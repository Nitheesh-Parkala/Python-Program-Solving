# 1)
print("*")
print("===========================")

# 2)
print()
print("===========================")

# 3)
for i in range(4+1):
    print("*")
print("===========================")

# 4)
for i in range(4+1):
    print("*",end=" ")
print() #This empty print statement is used to to cursor to next line.Other wise print("===========================") This particular statement is coming in same line.
print("===========================")

# 5)
#Rows:Because we cannot move the cursor back to the original position(in nested loop)
for i in range(1,4+1):
    #column
    for j in range(1,4+1):
        print("*",end=" ")
    print()
print("===========================================")

# 6)
# n=4
# i | j
# 1 | 1-4
# 2 | 1-4
# 3 | 1-4
# 4 | 1-4

n=4
for i in range(1,n+1):
    for j in range(1,n+1):
        print(i,end=" ")
    print()   
# O/p:
# 1 1 1 1
# 2 2 2 2
# 3 3 3 3
# 4 4 4 4
print("===========================================")



