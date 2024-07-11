'''Write a script in Python to read contents of a text file "poem.TXT", to
count and display the occurrence of those words which are having 5 or
more alphabets.'''
filename = "poem.TXT"
with open(filename, 'r') as file:
        c = file.read().lower().split()
        count = 0
        for char in c:
            if len(char)>=5:
                count+=1
        print('number of 5 or more letter words',count)