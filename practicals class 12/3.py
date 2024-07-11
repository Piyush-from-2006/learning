'''Define a function in Python that accepts Principle amount, rate of interest
and time as parameters and returns the simple interest as well as amount
Upon calculation.'''
amt = float(input("enter amount"))
int = float(input("enter interest"))
years = float(input("enter years"))
def simple_interest(amt,int,years):
    future_value = ((amt*int*years)/100) + amt
    simple_interest = ((amt*int*years)/100)
    print('simple interest: ', simple_interest)
    print('total value after interest: ',future_value)
simple_interest(amt,int,years)