'''Write a function to display the EndingA(names) to search and 
display those string from a list of names, which are ending with 
'A'
For e.g.
If the names contain of list is as follows:
List=['AMAN','SITA','LOKESH','RAMA']
The output should be: 
SITA
RAMA'''

def endingA(names):
    for i in range(len(names)):
        if (names[i][-1]) == 'A':
            print(names[i])
        else:
            continue
List=eval(input('enter a list of names: '))
endingA(List)