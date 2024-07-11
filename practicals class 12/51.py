'''Write a menu-based program in Python to perform the following tasks:
i) To input names of n- number of programming languages you know at
run-time from the user and write it to a pickled binary file
"LANG.DAT".
ii) To search whether the name of a given programming language is
present in the file or not.
iii) To remove the name of a given programming language (if exists)
from the file.
'''
import pickle as pkl
print("Menu")
print("1. Input Programming Languages")
print("2. Search for Language Name")
print("3. Remove Language Name")
choice = int(input("Enter your choice : "))
if choice == 1:
    n = int(input("How many languages do you know? "))
    lang_list = []
    for i in range(n):
        lang = input(f"Enter the {i+1}th language you know : ")
        lang_list.append(lang)
    with open('LANG.DAT', 'wb') as f:
        pkl.dump(lang_list, f)
if choice == 2:
    lang = input("Enter the language name you want to search : ")
    try:
        with open('LANG.DAT', 'rb') as f:
            data = pkl.load(f)
            if lang in data:
                print(f"{lang} is present.")
            else:
                print(f"{lang} is NOT present.")
    except EOFError:
        pass
if choice==3:
    lang = input("Enter the language name you want to delete : ")
    try:
        with open('LANG.DAT','rb') as f:
            data=pkl.load(f)
            if lang in data:
                data.remove(lang)
                with open('LANG.DAT','wb') as f:
                    pkl.dump(data,f)
                    print(f"{lang} has been deleted successfully.")
            else:
                print(f"Language {lang} was not found.")
    except EOFError:
        pass