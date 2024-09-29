#Manual function to split string into words.
def manual_split(str):
    words=[]
    word=""
    for char  in str:
        if char!=" ":
           word=word+char
        else:
            if word:
              words.append(word)
              word=""
    words.append(word)
    return words

def is_palindrome(word):
     i,j=0,len(word)-1
     while i<=j:
        if word[i] != word[j]:
           return False
        i+=1
        j-=1
     return True

def get_palindrome(str):
   words = manual_split(str)
   palindrome=[]
   for word in words:
      if is_palindrome(word):
         palindrome.append(word)
   return ' '.join(palindrome)

# Get and print the palindrome words
str="madam Mrs. Lee teaches malayalam"
palindrome_words = get_palindrome(str)
print(palindrome_words)

   