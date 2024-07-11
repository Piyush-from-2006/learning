'''
Write a script in Python to read each object of a pickled binary file
"DOCS.DAT" and display only those records where specialization of
doctors is "cardiology". Assume that the file "DOCS.DAT" is created with
the help of objects of <class 'dict'> type, with name and specialization of
hundreds of doctors stored into it as a key-value pairs.
'''
import pickle
f = open("DOCS.DAT",'rb')
print("Doctors with specialization in cardiology:")
try:
    while True:
        x = pickle.load(f)
        for i in x:
            if x[i].lower() == 'cardiology':
                print(i)
except EOFError:
    pass
f.close()