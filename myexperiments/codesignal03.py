# 3.Given the string, check if it is a palindrome.

def checkPalindrome(inputString):
    return inputString==inputString[::-1]
res=checkpalindrome("121")
print(res)
