'''Write a script in Python to count the total number of uppercase alphabets
present in a file "ABC.TXT"'''
filename = "ABC.TXT"
with open(filename, 'r') as file:
    uppercase_count = 0
    for char in file.read():
        if char.isupper():
            uppercase_count += 1
    print('uppercase character count',uppercase_count)
