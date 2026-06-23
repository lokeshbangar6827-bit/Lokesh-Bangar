s1=int(input("Enter sub 1: "))
s2=int(input("Enter sub 2: "))
s3=int(input("Enter sub 3: "))
s4=int(input("Enter sub 4: "))
s5=int(input("Enter sub 5: "))
print(s1)
print(s2)
print(s3)
print(s4)
print(s5)

total=s1+s2+s3+s4+s5
percentage = total/5

print("percentage = ",percentage)

if percentage>=90:
    print("Grade A")
    print("Distinction")
elif percentage>=75:
    print("Grade B")
    print("Pass")
elif percentage>=50:
    print("Grade c")
    print("Pass")
else:
    print("Grade= Fail")
    print("Fail")