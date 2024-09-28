#By doing Manually
str = "MY Name Is Nitheesh Prabhu"  # Input string
word = ""  # To hold the current word being processed
newStr = ""  # To hold the final reversed string
isFirstLetter = True  # A flag to identify the first letter of the word

for char in str:
    if char != " ":  # If character is not a space, keep building the word
        if isFirstLetter:
            # Make the first letter uppercase manually
            if 'a' <= char <= 'z':  # Check if it's lowercase
                word += chr(ord(char) - 32)  # Convert to uppercase
            else:
                word += char  # Keep it as it is (already uppercase)
            isFirstLetter = False  # The first letter is done
        else:
            # Make the rest of the letters lowercase manually
            if 'A' <= char <= 'Z':  # Check if it's uppercase
                word += chr(ord(char) + 32)  # Convert to lowercase
            else:
                word += char  # Keep it as it is (already lowercase)
    else:
        # We hit a space, meaning the word is complete and reversed
        newStr = word + " " + newStr  # Add the reversed word to the newStr
        word = "" 
        isFirstLetter = True  
newStr = word + " " + newStr  
print(newStr) 

print("=========================================")

#By USing Indexing
str="my name is nitheesh prabhu"
word=""
newStr=""
for char in str:
    if char!=" ":
       word=char+word
    else:
        newStr+=word[0].upper()+word[1:]+" "
        word=""
newStr=newStr+word[0].upper()+word[1:]
print(newStr)