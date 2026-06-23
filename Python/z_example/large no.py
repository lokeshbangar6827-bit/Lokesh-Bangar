num1=int(input("Enter no. 1: "))
num2=int(input("Enter no. 2: "))
num3=int(input("Enter no. 3: "))
print(num1)
print(num2)
print(num3)

if num1>=num2 and num1>=num3:
    print("largest no. is :",num1)
elif num2>=num1 and num2>=num3:
    print("largest no. is :",num2)
else:
    print("largest no. is :",num3)