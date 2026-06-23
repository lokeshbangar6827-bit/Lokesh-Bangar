# -----------------STAR-------------------------#
print("------------------------------------------------------")
n=int(input("enter no: "))

i=1

while i<=n:
    j=1
    while j<=n:
        print("*",end=" ")
        j+=1
    print()
    i+=1
    

n=int(input("Enter no: "))   
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()
print("-------------------------------------------------------")   
print("-------------------- 1 and 0 --------------------------")   
for i in range(n):
    for j in range(n):
        if i==j:
            print(1,end=" ")
        else:
            print(0,end=" ")
    print()
    
print("----------------------- X -------------------------------")   
for i in range(4):
    for j in range(4):
        if i==0 or i==3 or j==0 or j==3:
            print("X",end=" ")
        else:
            print(" ",end=" ")
    print()
print("----------------------------------------------------------")
        

    