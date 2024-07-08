#Write a script in Python to calculate the Profit/loss for a given cost price (CP) & selling price (SP)
cp=float(input("enter cost price: "))
sp=float(input("enter selling price: "))
if cp<sp:
    print("your profit is: ", str(sp-cp))
else:
    print("your loss is: ", str(cp-sp))
