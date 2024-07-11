'''data = {
    'Player1': [50,60,40,70],
    'Player2': [30,45,55,20],
    'Player3': [70,80,60,50],
}

with open("player.dat", 'wb') as f:
    import pickle
    pickle.dump(data, f)

print("Data saved to player.dat")
import pickle
with open ('avgrun.dat','rb') as f:
    try:
        while True:
            x = pickle.load(f)
            for i in x:
                print (i)
                print(x[i])
    except EOFError: pass
    '''
a,b=1
print(a+b)