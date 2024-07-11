'''Define a function calGCD_LCM() in Python that calculates the GCD and
LCM of two numbers passed to it as arguments'''
def calGCD_LCM(x,y):
    gcd=0
    for i in range (1,x+1):
        if x%i==y%i==0:
            hcf=i
    lcm=(x*y)/hcf
    print('gcd',hcf)
    print('lcm',int(lcm))
n1 = int(input("Enter a number: "))
n2 = int(input("Enter a number: "))
calGCD_LCM(n1,n2)
