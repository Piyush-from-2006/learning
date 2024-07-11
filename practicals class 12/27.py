'''Write a function to display the element of list thrice if it's a 
number and display the element terminated with '$' if it is not a 
number.
For e.g.
If the element content of list is as follows:
List=[23,”AZADI”,”AMRIT”,24,”MAHOTSAV”]
The output should be: 
232323
AZADI$
AMRIT$
242424
MAHOTSAV$'''

def display_element_thrice(list):
    for i in range(len(list)):
        if type(list[i]) is int:
            print(str(list[i])*3)
        else:
            print(list[i],end='$')
            print()
list=eval(input('enter a list: '))
display_element_thrice(list)
