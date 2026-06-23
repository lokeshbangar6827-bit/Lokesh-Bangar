# Reverse string
x="hello"
rev=""

for i in x:
    rev = i + rev
print("Reverse =",rev)

print("------------------------------------")

# Count Even and Odd character and Vowel...!!

x = "maharashtra"

even = 0
odd = 0
vowels = 0

for i in range(len(x)):  # i=0  x[0]=m 0%2==0t even=1 m= "aeiou"f vowel=0 odd=0
                         # i=1  x[1]=a 1%2==0f odd=1  a= "aeiou"t vowel=1 even=1
    if i % 2 == 0:       # i=2  x[2]=h 2%2==0t even=2 h= "aeiou"f vowel=1 odd=1
        even += 1        # i=3  x[3]=a 3%2==0f odd=2  a= "aeiou"t vowel=2 even=2 
    else:                # i=4  x[4]=r 4%2==0t even=3 r= "aeiou"f vowel=2 odd=2 
        odd += 1         # i=5  x[5]=a 5%2==0f odd=3  a= "aeiou"t vowel=3 even=3 
                         # i=6  x[6]=s 6%2==0t even=4 s= "aeiou"f vowel=3 odd=3 
    if x[i] in "aeiou":  # i=7  x[7]=h 7%2==0f odd=4  h= "aeiou"f vowel=3 even=4 
        vowels += 1      # i=8  x[8]=t 8%2==0t even=5 t= "aeiou"f vowel=3 even=4 
                         # i=9  x[9]=r 9%2==0f odd=5  r= "aeiou"f vowel=3 even=5 
                         # i=10  x[10]=a 10%2==0t even=6  a= "aeiou"t vowel=4 odd=5 
print("Even Count =", even)
print("Odd Count =", odd)
print("Vowel Count =", vowels)

print("------------------------------------")

# Uppercase 

x = "hello"
print(x.upper())

# without built-in fuction

x = "hello"
result = ""

for ch in x:
    result = result + chr(ord(ch) - 32)

print(result)       

        #  Iteration:
        # x=hello 
        # 1.ch=h ord(ch)=ord(h)=104 104-32=72 chr(72)=H res.="" + "H" result =H
        # 2.ch=e ord(ch)=ord(e)=101 101-32=69 chr(69)=E res.="H" + "E" result=HE
        # 3.ch=l ord(ch)=ord(l)=108 108-32=76 chr(76)=L res.="HE" +"L" result=HEL
        # 4.ch=l ord(ch)=ord(l)=108 108-32=76 chr(76)=L res.="HEL" +"L" result=HELL
        # 5.ch=o ord(ch)=ord(o)=111 111-32=79 chr(79)=O res.="HELL"+"O" result=HELLO
        
print("-------------------------------")

x = " hey"
y = ""

for ch in x:
    if ch != " ":
        y += ch

print("String =", y)
print("Length =", len(y))

print("-----------------------------")

x = "python programming"
result = ""

for ch in x:

    if ch == 'p':
        result = result + 'x'
    else:
        result = result + ch

print(result)

print("-----------------------------")

# slising 

x="India"
print(x[3:5])
print(x[3:])
print(x[0:3])
print(x[:3])
print(x[1:4])
print(x[0:5:2])

x="India is my country"
print(x[6:8])
print(x[12:17])
print(x[7:10])
print(x[16:])
print(x[-9:-15:-1])
print(x[::-1]) #<--reverse string

x = "Python"

print(x[5:0:-1])
print(x[-1:-7:-1])

# Palindrome...!!

# ip=input("Enter string: ")
# if ip==ip[::-1]:
#     print("palindrome")
# else:
#     print("Not palindrome")
    
    
x="abc1234"

ct1=0
ct2=0
for ch in x:
    if ch>='0' and ch<='9':
        ct1 +=1
    elif (ch>='a' and ch<='z') or (i>='A' and i>='Z'):
        ct2+=1
print("Count of digit: ",ct1)
print("count of alpha is: ",ct2)

print(f"count of digit: {ct1}\n count of char: {ct2}")


x="swapcase"
new_str=""
for i in x:
    if i>='a' and i<='z':
        new_str += chr(ord(i)-32)
print(new_str)

x="LOKESH"
new_str=""
for i in x:
    if i>='A' and i<='Z':
        new_str += chr(ord(i)+32)
print(new_str)

x="LokEsH"
new_str1=""
new_str2=""
for i in x:
    if (i>='A' and i<='Z'):
        new_str1 += chr(ord(i)+32)
    elif(i>='a' and i<='z'):
        new_str2 += chr(ord(i)-32)
print(f"new_str: {new_str1}\n new_str2: {new_str2}")


x="LokEsH"
new_str=""
for i in x:
    if (i>='A' and i<='Z'):
        new_str += chr(ord(i)+32)
    elif(i>='a' and i<='z'):
        new_str += chr(ord(i)-32)
print(new_str)


x="programming"

for i in x:
    if ord(i)%2!=0:
        print(i,ord(i))
        
print("-----------------------------")        
x="programming"

if ord(i)%2==0:
    print(i,ord(i))
    
x="Programming"
unique=""

for ch in x:
    if ch not in unique:
        unique+=ch
        print(unique)
print(unique)

print("--------------------------------")

x="I like python programming"
ct=1

for i in x:
    if ' ' in i:
        ct+=1

print(ct)


s = "india is my country"
result=""

for ch in s:
    if ch>= 'a' and ch<= 'z':
        result+=chr(ord(ch)-32)
    else:
        result+=ch
print(result)

s = "india is my country"
result=""

for ch in s:
    if ch>= 'A' and ch<= 'Z':
        result += chr(ord(ch)+32)
    else:
        result+=ch
print(result)






















