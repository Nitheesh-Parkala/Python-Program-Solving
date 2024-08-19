#Function is a block of code designed to execute a particular task
#A function is not be executed until or unless it not been called.

def checkEvenOdd(n):  #Function declaration
    if(n%2==0):       #Body / definition/scope of a function
        return True
    return False

num=int(input("Enter a value "))
flag=checkEvenOdd(num)   #function call
if flag==True:
    print("The Number is Even")
else:
    print("Number is odd")

#Terminology.

# 1.parameter-> It is a input required by the function to execute the logic. It is included with function declaration,it is a local variable
# 2.Arguments-> It is a value or  a variable holding value which is given to a function during the function call on which the logic is perform
# 3. flag-> it is just a standard variable name  used to hold the boolean value,return by the function
# 4. return-> helps to return a value from the called function back to the function call and 
# it also returns the execution flow from the called function back to the place from were it is called even if the porgrmmaer doesn't include return statement the python cmpl include its.