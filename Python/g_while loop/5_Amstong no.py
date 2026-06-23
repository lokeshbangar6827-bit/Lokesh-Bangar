num=int(input("enter no.."))
temp=num
sum=0
ct=0
while temp>0:
    ct+=1
    temp//=10
print(ct)
temp=num
while temp>0:
    rem =temp%10
    sum+=(rem**ct)
    temp//=10

if num==sum:
    print("Armstrong no..")
else:
    print("Not Armstrong no...")