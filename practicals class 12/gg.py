# x="Come let us have some fun"
# l=x.split()
# t=()
# print(l)
# for i in l:
#     t=t+(len(i),)
# print(t)
# for i in range (5): print(i)
s='lost'
l=[10,21,33,4]
d={}
for i in range(len(l)):
    if i%2==0: d[l.pop()]=s[i]
    else: d[l.pop()]=i+3
for k,v in d.items():
    print(k,v, sep=':')