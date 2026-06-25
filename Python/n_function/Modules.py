import math

print(math.sqrt(25))
print(math.factorial(5))
print(math.ceil(45.78))
print(math.floor(89.45))
print(math.pow(2,3))
print(math.pi)

calc=2*math.pi*2
print(calc)

print("-------------------------------------------------------")

import random as r

print(r.randint(1000,9999)) #--->int
print(r.random()) #0.0 to 1.0 --->float
print(r.randrange(1,10,2))

x=["Red","black","blue","pink"]
print(r.choice(x))
print(r.choices(x,k=2))
r.shuffle(x)
print(x)