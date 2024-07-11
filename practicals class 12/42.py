'''
Write a script in Python to display all those lines from a file
"BAKERY.TXT" which has "Chocolate" word anywhere in it.
'''
with open("BAKERY.TXT", 'r') as file:
    for line in file:
        if "Chocolate" in line: print(line)