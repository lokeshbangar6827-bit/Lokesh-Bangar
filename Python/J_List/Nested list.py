S=[
    [101,"Ram",98],
    [102,"sita",88],
    [103,"Ramu",78],
    [104,"gita",99]
]

for i in S:
    print(i[0]) 
    print(f"{i[1]}---> {i[2]}")
    
data=[105,"komal",55]
S.append(data)
print(S)

id=int(input("enter id: "))
name=input("enter name: ")
marks=int(input("enter marks: "))

S.append([id,name,marks])
print(S)

print("-------------------------------------")

while True:
    print("SMS\n1.add\n2.view\n3.update\n4.delete\n5.Topper\n6.exit\n")
    choice=int(input("enter yr choice: \n"))
        




