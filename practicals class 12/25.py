'''Write a function countNow(PLACES) in Python, that takes the 
dictionary, PLACES as an argument and displays the names (in 
uppercase)of the places whose names are longer than 5 
characters. 
For example, Consider the following dictionary 
PLACES={1:"Delhi",2:"London",3:"Paris",4:"New 
York",5:"Doha"} 
The output should be: 
LONDON 
NEW YORK '''

def countNow(PLACES):
    for i in PLACES:
        if len(PLACES[i]) > 5:
            print(PLACES[i].upper())
PLACES={1:"Delhi",2:"London",3:"Paris",4:"New York",5:"Doha"}
countNow(PLACES)