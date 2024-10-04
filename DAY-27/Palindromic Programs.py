def filtration(s1):
    nstr = ""

    for i in range(len(s1)):
        if "A" <= s1[i] <= "Z":
            nstr += chr(ord(s1[i])+32)
        elif "a" <= s1[i] <= "z" or "0" <= s1[i] <= "9":
            nstr += s1[i]
    return nstr


def checkPalindrome(s1):
    s1 = filtration(s1)
    i, j = 0, len(s1)-1

    while i <= j:
        if s1[i] != s1[j]:
            return False
        i += 1
        j -= 1
    return True

def displayPalindromicWrd(s1):
    nwrd = ""
    palindromic = []

    for i in range(len(s1)):
        if s1[i] != " ":
            nwrd += s1[i]
        else:
            flag = checkPalindrome(nwrd)
            if flag:
                palindromic.append(nwrd)
            nwrd = ""

    return palindromic

def printLongestPalindrome(s1):
    nwrd = ""
    max = -2147483648
    longest = ""

    for i in range(len(s1)):
        if s1[i] != " ":
            nwrd += s1[i]
        else:
            flag = checkPalindrome(nwrd)
            if flag:
                if max < len(nwrd):
                    longest = nwrd
                    max = len(longest)
            nwrd = ""

    return longest, max

def printShortestPalindrome(s1):
    nwrd = ""
    min = 2147483648
    shortest = ""

    for i in range(len(s1)):
        if s1[i] != " ":
            nwrd += s1[i]
        else:
            flag = checkPalindrome(nwrd)
            if flag:

                if min > len(nwrd):
                    shortest = nwrd
                    min = len(shortest)
            nwrd = ""

    return shortest, min

def countContinuousPalindromes(s1):
    nwrd = ""
    count = 0
    max_val = []

    for i in range(len(s1)):
        if s1[i] != " ":
            nwrd += s1[i]
        else:
            flag = checkPalindrome(nwrd)
            if flag:
                count += 1
            else:
                count = 0
            nwrd = ""
            if count > 0:
                max_val.append(count)

    val = -2147483648
    for i in max_val:
        if val < i:
            val = i
    return val


s1 = input("Enter str: ")
res = displayPalindromicWrd(s1+" ")
print(res)
res, max = printLongestPalindrome(s1+" ")
print(res, " ", max)
res, min = printShortestPalindrome(s1+" ")
print(res, " ", min)
max = countContinuousPalindromes(s1+" ")
print(max)