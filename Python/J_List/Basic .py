x=[10,20,30]
#access 20
print(x)
print(x[1])
#update:refvar[index]=new_value
print(x[2])
x[2]=300
print(x[2])

print("-------------------------------")

x=[10,20,30]

for items in x:
    print(items)
    
x=[]
print(x)
x.append(10)
print(x)
x.append(20)
print(x)

print("--------------------------------")

#using loop
#add element by taking user ip
x=[]
print(x)
for i in range(5):
    ip=input(f"enter {i+1} element")
    x.append(ip)
print(x)

print("----------------------")

#extend--->items by separater]
x=[1,2]
print(x)
x.extend([3,4])
print(x)

print("----------------------------------")

#insert (index,value)
x=[11,13]
#0  1---> 0 1 2
x.insert(1,12)
print(x)

print("-----------------------------")
#remove(element)/pop(index)
x=[10,8,9,"hi",90,89]
x.remove("hi")
x.pop(4)
print(x)
x.clear()
print(x)

print("-----------------------------")

x=[10,20,30,40,30]
print(x.count(30))
print(x.index(20))
x.sort()
print(x)
x.reverse()
print(x)
y=x.copy()
print(y)

print("---------------------------")

#fuction
x=["hi",20,40,8]
print(len(x))
print(max(x))
print(min(x))
print(sum(x))
print(sorted(x,reverse=True))

