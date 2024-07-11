'''
Write a script in Python to read each object of a pickled binary file
"STOCK.DAT" and display the Name from all such records whose Price is
above 150. Assume that the file "STOCK.DAT" is created with the help of
objects of <class ‘dict’> type, with name and price as key- value pairs.
'''
import pickle
with open("stock.DAT", 'rb') as f:
    print("Brands with price more than 150:")
    try:
        while True:
            x = pickle.load(f)
            for i in x:
                if x[i] > 150 : print(i)
    except EOFError: pass