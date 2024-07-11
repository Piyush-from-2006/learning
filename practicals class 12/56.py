'''
Write a script in Python to read each record from a CSV file "trains.csv"
and display the name(s) of only those trains whose source of origin is
Delhi and destination is Vizag. Assume that the file 'trains.csv' consists of
data of hundreds of trains in tabular format under the heads:
[TrainNo, TrainName, Source, Destination, Fare]
'''
import csv
i_f = "trains.csv"
with open(i_f, 'r') as cf:
    next(cf)
    for r in csv.reader(cf):
        if r[2].strip().lower() == 'delhi' and r[3].strip().lower() == 'vizag':
            print(r[1])
