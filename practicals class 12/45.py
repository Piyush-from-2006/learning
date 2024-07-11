'''
Write a script in Python to search whether a name “Neha” is present or
not in a pickled binary file “STU.DAT” that consists of data of hundreds of
students stored as objects of class dict in {Rollno : Name} format.
'''
import pickle
with open("STU.DAT", 'rb') as f:
    condition = False
    try:
        while True:
            x = pickle.load(f)
            if 'neha' in x.values():
                condition = True
    except EOFError: pass
if condition: print("Neha Found!")
else: print("Not found!")
