x=input("enter a string")
a=x[0]
for i in x:
    if i==a:
        x=x.replace(i,'$')
        x=a+x[1:]
print(x)