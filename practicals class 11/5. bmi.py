#Write a script in Python to calculate BMI (Body Mass Index) of a person.
height = float(input("Input your height in metre: "))
weight = float(input("Input your weight in Kilogram: "))
print("Your body mass index is: ", weight / (height * height))