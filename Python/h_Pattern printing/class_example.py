for i in range(1,4):
    for j in range(1,4):
        
        if (i+j)%2==0:   #Because the pattern alternates.
            print("X",end=" ")
        else:
            print("O",end=" ")
    print()
    
print("--------------------------------------------------")

for i in range(1,4):
    ch=chr(96 + i)
    for j in range(1,4):
        print(ch,end=" ")
    print()
    
print("---------------------------------------------------")

ch = 97

for i in range(1, 4):
    for j in range(1, 5):

        print(chr(ch), end=" ")

        ch += 1
    print()
    
print("----------------------------------------------------")

for i in range(1, 4):

    num = 1

    for j in range(1, 4):
        print(num, end=" ")
        num += 1

    print()

print("-----------------------------------------------------")

num = 9
for i in range (1,4):
    for j in range(1,4):
        print(num,end=" ")
        num -=1
    print()
    
print("-----------------------------------------------------")

ch = 65   # ASCII of 'A'

for i in range(1, 4):
    for j in range(1, 4):
        print(chr(ch), end=" ")
        ch += 2
    print()
    
print("------------------------------------------------------")

for i in range(1, 5):
    for j in range(1, 5):

        if i == 1 or i == 4 or j == 1 or j == 4:
            
            # corners
            if (i == 1 and j == 1) or (i == 1 and j == 4) or (i == 4 and j == 1) or (i == 4 and j == 4):
                print("O", end=" ")
            else:
                print("X", end=" ")
        
        else:
            print(" ", end=" ")

    print()
    
print("----------------------------------------------------")

for i in range(1,6):
    for j in range(1,6):
        
        if ((i==1 or i==5 or j==1 or j==5)or(i==3 and j==3)):
            print("0",end=" ")
        else:
            print("1",end=" ")
    print()
    
    
print("-----------------------------------------------------------------------------------------------")


# L letter 

for i in range(5):
    for j in range(4):
        if j==0 or i==4:     #(j==0 or i==4) or (j==0 or i==4) or j==3 or i==4:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print() 
    
print("-------------------------------------------------------------------")
    
for i in range(5):
    for j in range(4):
        if (i==0 or i==2 or i==4):
            print("*",end=" ")
        elif(j==0 or j==3):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print() 
    
print("-----------------------------------------------------------------------")

for i in range(5):
    for j in range(5):
        if i==0 or i==4 or j==0 or j==4 or i==j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print("----------------------------------------------------------------------")

for i in range(1,4):
    for j in range(i):
        print("*",end=" ")
    print()
    
for i in range (2,0,-1):
    for j in range(i):
        print("*",end=" ")
    print("")
    
print("------------------------------------------------------------")
   
num = 1

for i in range(1,5):
    for j in range(i):
        print(num,end=" ")
    print()
    num+=2

num=5    
for i in range(3,0,-1):
    for j in range(i):
        print(num,end=" ")
    print()
    num-=2
    
print("--------------------------------------------------------------------")
    



    
    

    
    
