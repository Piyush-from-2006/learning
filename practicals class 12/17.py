'''Define a function in uprCount(S) in Python that accepts a string (S) as
parameter and returns the total number of uppercase alphabets present in
it.
e.g. if the string is, S= "Hello ALL"
then the function should return count as: 4'''
def uprCount(S):
    count = 0
    for i in range(len(S)):
        if S[i].isupper():
            count += 1
    print(count)
uprCount("Hello AlL")