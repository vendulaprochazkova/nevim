jidlo = ["chleba","sushi","kebab","coko","neco mnam"]
x = len(jidlo)
print = (len(jidlo)) 
for x in jidlo:
    print(x)
new = input("zadejte novou papu")
jidlo.append(new)
print(len(jidlo))
jidlo.pop(4)
jidlo.sort()
jidlo.reverse()
for x in jidlo:
    print(x)
    