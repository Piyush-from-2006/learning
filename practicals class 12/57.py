'''
Write a script in Python to export the data of all football players from a file
"players.csv" to a new file "football.csv". Assume that the "players.csv" file
stores data of hundreds of players in tabular form under the following
heads:
[SNo, Player_name, gender, game, category]
'''
import csv
i_f, o_f, f_p = "players.csv", "football.csv", []
with open(i_f, 'r') as cf:
    next(cf)
    for r in csv.reader(cf):
        if r[3].strip().lower() == 'football':
            f_p.append(r)
with open(o_f, 'w', newline='') as cf:
    w = csv.writer(cf)
    w.writerows([r for r in f_p])
print("Football player data exported to", o_f)
