num=int(input("Enter num: "))
temp=num
rev=0
while num>0:
    rem=num %10
    rev=(rev*10)+rem
    num //=10

if temp==rev:
    print("pallindrome..")
else:
    print("Not pallindrome")