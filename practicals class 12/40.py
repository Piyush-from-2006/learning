'''
Write a script in Python to find and display the longest line (i.e. a line with
maximum no. of characters) present in a text file "STORY.TXT". Also,
display the length of the longest line
filename = "STORY.TXT"
'''
with open('abc.TXT', 'r') as file:
    longest_line = ""
    max_length = 0
    for line in file:
        line_length = len(line)
        if line_length > max_length:
            max_length = line_length
            longest_line = line
    print("Longest line:")
    print(longest_line.strip())
    print("Length of the longest line:", max_length)