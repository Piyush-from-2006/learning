'''Define a function COUNTNOW(PLACES) to find and display those place
names, in which there are more than 5 characters.
e.g. If the list PLACES= ["DELHI", "LONDON", "PARIS", "NEW YORK" ]
Then the function should display the following names:
LONDON
NEW YORK'''
def COUNTNOW(PLACES):
    for place in PLACES:
        if len(place) > 5:
            print(place)
PLACES=eval(input('enter a list of places: '))
COUNTNOW(PLACES)