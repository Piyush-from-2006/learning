'''
Write a script in Python to read all records from a csv file "TRAVEL.CSV"
and segregate all such travel destinations that falls in India by exporting
their names to a plain text file "INDIAN.TXT". Assume that the
"TRAVEL.CSV" file consists of hundreds of names of travel destinations
along with the name of the country to which they belong to.
'''
import csv
lst =  []
with open('travel.csv', 'r') as f:
    r = csv.reader(f)
    for row in r: 
        d,c=row[0],row[1]
        if c.strip().lower() == 'india': lst.append(d)
with open('indian.txt', 'w') as f:
    for d in lst: f.write(d + '\n')
print("Indian destinations exported to indian.txt")
