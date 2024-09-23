def checkLowerCase(s1):
    newStr = ""
    for i in range(len(s1)):
        data = s1[i]
        intger = ord(data)
        if 65 <= intger <= 90:  # Check if it's an uppercase letter (A-Z)
            newIntger = intger + 32  # Convert to lowercase by adding 32
            newChar = chr(newIntger)
            newStr += newChar
        elif 97 <= intger <= 122:  # Check if it's a lowercase letter (a-z)
            newIntger = intger - 32  # Convert to uppercase by subtracting 32
            newChar = chr(newIntger)
            newStr += newChar
        else:
            newStr += data  # If not a letter, add the character as is
    return newStr

s1 = input("Enter a String: ")
res = checkLowerCase(s1)
print(res)
