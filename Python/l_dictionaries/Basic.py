# k:v
# mutable
# key should be unique
# value-duplicate
# {}

x={}
print(x,type(x))
# add --->refvar[key]=value
x["rollno"]=101
x["name"]="ram"
print(x)

# access --->x[key]--->value
print(x["name"])

# update --->ref[key]=newvalue
x["name"]="sita"
print(x["name"])

print("---------------------------------------")

stud={
    "rollno":101,
    "name":"ram",
    "age":30,
    "sub":["math","eng"]
}
print(stud)

print("----------------------------------------")
# Methods
print(stud.keys())
print(stud.values())
print(stud.items())

print("----------------------------------------")
# loops
for key in stud:
    print(key)
    
for values in stud.values():
    print(values)
    
for k,v in stud.items():
    print(k,v)
    
for v in stud["sub"]:
    print(v)
    
for key in stud:
    if key =="sub":
        for v in key:
            print(v)
    
    
