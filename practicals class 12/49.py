'''
Write a script in Python to read each object of a pickled binary file
"CALL.DAT" and display the data of such objects where the duration of
call (in minutes) is maximum. Assuming that the file consists of data of
objects of class tuple in the format: (name, duration)
'''
import pickle
dur, user, f = 0, "", open("CALL.DAT",'rb')
try:
    while True:
        x = pickle.load(f)
        if x[1] > dur:
            user = x[0]
            dur = x[1]
except EOFError: pass
f.close()
print("Maximum duration: ",dur," minutes")
print("User: ",user)