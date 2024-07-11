'''Define a function in Python that checks for the presence of all prime
numbers between a given range.'''
start = int(input("Enter start number: "))
end = int(input("Enter end number: "))

def check_primes(start, end):
    primes = []
    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                primes.append(num)
    print(primes) 
check_primes(start,end)