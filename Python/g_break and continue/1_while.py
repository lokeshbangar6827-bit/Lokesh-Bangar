
# i=1

# while i<=10:
#     print(i)
    
#     if i==5:
#         break
#     i+=1
    
    
# i=1

# while i<=10:
#     print("checking",i)
    
#     if i==8:
#         print("Found 8")
#         break
#     i+=1
    
    
# password = 1234

# while True:
#     user_password = int(input("Enter password: "))

#     if user_password == password:
#         print("Access Granted")
#         break
    
    
# ---------------------------------------------------------------------#
#---------------------------Continue-----------------------------------#

i = 0

while i < 5: #0<5 t ,1<5 t ,2<5 t 4<5 t  5<5 f
    i += 1

    if i == 3: #i=3 = skip 
        continue

    print(i) #1,2,4,5 
    
    
i = 1

while i <= 10:
    if i == 5:
        i += 1
        continue

    print(i)
    i += 1
    
i=1 
   
while i<=10:
    if i%2 ==0:
        i+=1
        continue
    print(i)
    i+=1