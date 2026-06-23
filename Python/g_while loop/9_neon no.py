num=9
sq=num ** 2
sum=0

while sq >0:
    
    rem =sq%10
    sum +=rem 
    sq //=10
    
if num == sum:
    print("Neon no..")
else:
    print("Not Neon no..")