#Write a prg to print  1-4  
# A) No loops allowed
# B) Maintain the coding standards

def printMsg4(n):
    print(n)  #4

def printMsg3(n):
    print(n)  #3
    printMsg4(4)

def printMsg2(n):
    print(n) #2
    printMsg3(3)


def printMsg1(n):
    print(n) #1
    printMsg2(2)

printMsg1(1)
#stack->> It is a temporary memory present in PVM.
# It stores the current executing block of code with its and allocates the memory for local variables.
# - As the memory is allocated for the block of  code when it is called,
# it is also required to deallocate the emory with a return statement after execution of that code.
