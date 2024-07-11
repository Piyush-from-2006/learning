'''
Write a script in Python to read each object of a pickled binary file
"PLAYER.DAT" and export the name and average runs scored by each
player to another file "AVGRUN.DAT". Assume that the file
"PLAYER.DAT" is created with the help of objects of <class ‘dict’> type
with player name and a list of runs scored by a player in different matches
he played as key-value pairs.

'''
import pickle
f1 = open("PLAYER.DAT",'rb')
f2 = open("AVGRUN.DAT",'wb')
try:
    while True:
        x = pickle.load(f1)
        for i in x:
            avg = sum(x[i])/len(x[i])
            pickle.dump({i:avg}, f2)
except EOFError:
    pass
f1.close()
f2.close()
print("Exported average runs to AVGRUN.DAT")