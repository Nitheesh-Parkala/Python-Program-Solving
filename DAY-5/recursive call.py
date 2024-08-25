#Write a prg to print  1-4  using recursive function 
# A) No loops allowed
# B) Maintain the coding standards

def printMsg1(n):
    #base condition
    if(n>4):
        return
    print(n)
    #recursive call
    printMsg1(n+1)

#Initial function call
printMsg1(1)

print("=============================================")
def printMsg1(n):
    if(n>4):
        return
    printMsg1(n+1)
    print(n)

#Initial function call
printMsg1(1)
