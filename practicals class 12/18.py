'''Define a function in vowCount(S) in Python that accepts a string (S) as
parameter and returns the total number of vowels present in it.
e.g. if the string is, S= "Hello All"
then the function should return count as: 3'''
def vowCount(S):
    S=S.lower()
    count = 0
    for i in range(len(S)):
        if S[i] in 'aeiou':
            count += 1
    print(count)
vowCount("Hello All")
