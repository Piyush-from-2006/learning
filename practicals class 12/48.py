'''
Write a script in Python to read each object's data from a pickled binary
file "PLACES.DAT" and display the data of only such places where the
number of Covid-19 cases are more than 500. Assume that the file
"PLACES.DAT" is created with the help of objects of <class 'dict'> with
name of the place and number of cases stored as a key-value pairs.
'''
import pickle
f = open("PLACES.DAT",'rb')
print("Places with more than 500 covid-19 cases:")
try:
    while True:
        x = pickle.load(f)
        for i in x:
            if x[i] > 500:
                print(i)
except EOFError: pass
f.close()