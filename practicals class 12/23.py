'''Define a function update(d, k, v) in Python that accepts a key-value pair
(k:v) as parameter and adds it to the dictionary (d) only if the key (k) is not
present in it, otherwise give key exists message.
e.g. if d={1: "India", 2: "USA", 3: "Japan", 4: "Israel" }
then a call update(d, 5, "Russia") should add it to the dictionary d,
whereas a call update(d, 3, "Bhutan") gives a message "Key Exists!"'''
def update(d, k, v):
    if k in d:
        print("Key Exists!")
    else:
        d[k] = v
        print(d)
d = {1: "India", 2: "USA", 3: "Japan", 4: "Israel"}
update(d, 5, "Russia")
update(d, 5, "Russia")