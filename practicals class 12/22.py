'''Define a function spell(num) in python that accepts a number as
parameter and returns its equivalent word form with spelling of each digit
of the number.
e.g. if num=143
then the function should return: "ONE FOUR THREE"'''
def spell(num):
    digits = ['ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE']
    spelled = ''
    for d in str(num):
        spelled += digits[int(d)] + ' '
    print(spelled.strip())
num=234765

spell(num)