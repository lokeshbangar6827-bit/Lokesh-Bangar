# 1. How many rows?

# *
# * *
# * * *
# * * * *
# Rows = 4

# so, 
# for row in range(1,5)

# 2. How many items in each row?

# Row 1 → 1 star
# Row 2 → 2 stars
# Row 3 → 3 stars
# Row 4 → 4 stars

# so,
# for col in range(1, row + 1):


print("-------------------Star Triangle ---------------------")

for i in range (1,5):
    for j in range (1,i+1):
        print("*",end=" ")
    print()
    
print("-------------------------------------------------------")

for i in range (4,0,-1): #range(start,end,step)
    for j in range (1,i+1):
        print("*",end=" ")
    print()
print("--------------------------------------------------------")   


# Structure :

# for i in range(rows):
#     for j in range(cols):
#         print(...)
