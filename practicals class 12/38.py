'''Write a script in Python to read all lines from a file "MSG.TXT" and display
only those lines that starts with either alphabet 'A' or alphabet 'T'.
'''
filename = "msg.txt"
with open(filename, 'r') as file:
    for line in file:
        if line[0].upper() == 'A' or line[0].upper() == 'T':
            print(line.strip())
