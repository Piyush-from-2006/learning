'''Define a function checkPalindrome() in python that accepts a string as
parameter and checks whether string is palindrome or not.'''
def checkPalindrome(s):
    print (s == s[::-1])
s=str(input('enter anything'))
checkPalindrome(s)