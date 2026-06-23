num=1124
sum=0
mul=1

while num>0:
    
    rem=num%10
    sum +=rem
    mul *=rem
    num //=10
    
if sum == mul:
    print("Spy no.")
else:
    print("Not spy no")