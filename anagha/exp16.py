a=int(input("enter the number of elements:"))
print("enter the elements:")
li=[]
for i in range(0,a):
    el=int(input())
    if (el>100):
        el="over"
        li.append(el)
    else:
        li.append(el)
print(li)






