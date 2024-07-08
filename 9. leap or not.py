'''Write a script in Python to input a calendar year and to check if it is a leap year or not.
Hint: A year is a leap year if it is divisible by 4, except that years divisible by 100 are
not leap years unless they are also divisible by 400'''
year = int(input("Enter a calendar year: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(year, "is a leap year.")
        else:
            print(year, "is not a leap year.")
    else:
        print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")

