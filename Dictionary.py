d={110:"raj",120:"vivek",130:"nikunj",140:"prince",150:"arth"}
print(d)
d[130]="jigar"
print(d)
#d.clear()
#print(d)
d.get(110)
print(d)
print(d.items())
print(d.keys())
print(d.values())
print(d.pop(150))
print(d)
print(d.popitem())
d1={160:"vicky",170:"jay"}
d.update(d1)
print(d)

d={110:"raj",120:"vivek",130:"nikunj",140:"prince",150:"arth"}
for i in d:
    print(i," : ",d.get(i))
    
print("****************")

for i in d:
    print(i," : ",d[i])


d={}
n=int(input("enter n :"))
for i in range(n):
    d[i]=i*i
print(d)

d1={"A":100,"B":200,"c":300}
d2={"A":100,"B":200,"D":400,"E":500}
d3={}

for i in d1:
    if i in d2:
        d3[i]=d1[i]
print(d3)

d1={"A":100,"B":200,"C":300,"E":500}
d2={"A":100,"B":200,"D":400,"E":500}
d3={}

for i in d1:
    if i in d2:
        d3[i]=d1[i]
print(d3)








    
