t=(1,2,1.1,2.2,"tops",[10,20,30],True,"python",1,1,False)

print(t)
print(t.count(1))
print(t.index(0))

for i in t:
    print(i)
print(t[5])
t[5].append(40)
print(t)
print(10 in t)
