name ="ram"
print(name)
print(id(name))
print(name[0])
# name[0]='p'
name="sita"
print(name)
print(id(name))

# given string-->fetch one by one 
for ch in name:
    print(ch)

#Length... 
X="Maharashtra"
print(len(X))

print("------------------------------")

#Reverse...
for ch in range(len(X)-1,-1,-1):
    print(X[ch])
    
x="India"

ct=0
for ch in X:
    ct+=1
print(ct)

# Methods

print("-----------------Upper and lower-----------------------")
X="India"
print(X.upper())
print(X.lower())

print("--------------Title and capitalize---------------------")
x="how are you"
print(x.title())
print(x.capitalize())

print("--------------------Swap case and replace-----------------")

x="india"
print(x.swapcase())
print(x.replace('dia','x'))
print(x.replace('i','S'))  

print("----------------Count character,index,split,find---------------")

x= "Lokesh"
print(x.count('e'))
print(x.index('k')) 
print(x.find('v'))
print(x.split(' , '))

# checking method -->true or false

x="HELLO"
print(x.isupper())
print(x.islower())

# checking ---> all alphabets
print(x.isalpha())

x="1234"
print(x.isdigit())

# alpha+num
x="al123"
print(x.isalnum())

print(x.startswith("al"))
print(x.endswith("4"))

# white spaces -->remove
x="  hello"
print(len(x))

x=x.strip()
print(len(x))


name = "Python"

print(name[0])
print(name[2])
print(name[-1])

