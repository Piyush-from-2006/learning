'''Write a script in Python to read the contents of a file "SCHOOL.TXT" and
copy all occurrences of the words 'handball', 'football', 'basketball'
(irrespective of the letter-case) to a NEW file "SPORTS.TXT"'''
with open("SCHOOL.TXT", "r") as source_file:
    with open("SPORTS.TXT", "w") as target_file:
        for line in source_file:
            words = line.lower().split()
            for word in words:
                if word in ['handball', 'football', 'basketball']:
                    target_file.write(word + '\n')
