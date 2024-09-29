
def get_manualsplit(str):
    words=[]
    word=""
    for char in str:
        if char!=" ":
            word=word+char   
        else:
            if word:
                words.append(word)
                word=""
    words.append(word)
    return words  

def check_plaindrome(word):
    i,j=0,len(word)-1
    while(i<=j):
        if word[i]!=word[j]:
            return False
        i+=1
        j-=1
    return True

def get_palindrome(str):
    words=get_manualsplit(str)
    palindrome=[]
    for word in words:
      if check_plaindrome(word):
          palindrome.append(word)
    return palindrome
          

str="madam Mrs. Lee teaches malayalam"
res=get_palindrome(str)

smallest_palindrome=""
for word in res:
    if  len(word)<len(smallest_palindrome):
        smallest_palindrome=word

print(word)