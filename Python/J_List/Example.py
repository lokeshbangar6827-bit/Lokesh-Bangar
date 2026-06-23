# Check element

X = [101,57,6,98,32,10,57,98]

key = 98
found = False

for i in X:
    if i == key:
        found = True
        break

if found:
    print("Key found")
else:
    print("Key not found")

print("---------------------------------------")
   
#Duplicate Elements:....

X = [101,57,6,98,32,10,57,98]

dup = []

for i in X:
    if X.count(i) > 1 and i not in dup:
        dup.append(i)

print(dup)

print("---------------------------------------")

# Unique element:....

X = [101,57,6,98,32,10,57,98]

for i in X:
    if X.count(i) == 1:
        print(i, end=" ")

print("---------------------------------------")
       
# Sort Without Using sort()

X = [101,57,6,98,32,10,57,98]

n = len(X)

for i in range(n):
    for j in range(n-1-i):
        if X[j] > X[j+1]:
            X[j], X[j+1] = X[j+1], X[j]

print(X)

print("---------------------------------------")

# Even , Odd:....

X = [101,57,6,98,32,10,57,98]

even = 0
odd = 0

for i in X:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even =", even)
print("Odd =", odd)