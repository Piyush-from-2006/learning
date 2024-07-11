'''
Write a script in Python to count total number of lines that begins with the
word "the" in a file "POEM.TXT"
filename = "POEM.TXT"
search_word = "the"
'''
count = 0
with open('poem.txt', 'r') as file:
    for line in file:
        if line.strip().lower().startswith('the'): count += 1
print("Total number of lines starting with 'the':", count)
