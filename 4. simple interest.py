'''Write a script in Python to input the values of principal amount,
rate of interest and time from user and compute the simple interest '''
amt = float(input("enter amount"))
int = float(input("enter interest"))
years = float(input("enter years"))
future_value = ((amt*int*years)/100) + amt
simple_interest = ((amt*int*years)/100)
print('simple interest: ', simple_interest)
print('total value after interest: ',future_value)