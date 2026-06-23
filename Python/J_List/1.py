x=[10,20,45,7]
print(sum(x))
sum=0
for i in x:
    sum+=i
print(sum)

print("------------------------------")

x=[10,20,40,45,50]
print(len(x))
ct=0
for i in x:
    ct+=1
print(ct)

print("------------------------------")

x=[10,20,30,40]
max=0
for i in x:
    if i>max:
        max=i
print(max)

print(min(x))
min=0
for i in x:
    if i<min:
        min+=1
print(min)

print("------------------------------------")

student=[1,"ram",2,"sita",3,"pooja"];
print(student)
for i in range(len(student)):
    if i%2==0:
        print(student[i])
        
print("-------------------------------------------")

students = [
    ["Ram", 1, 45],
    ["sita",2, 78],
    ["Pooja",3, 90]
]

for student in students:
    print("Name :", student[0])
    print("ID   :", student[1])
    print("Marks:", student[2])
    print()

