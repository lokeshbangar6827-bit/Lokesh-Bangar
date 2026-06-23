salary=int(input("Enter salary: "))
exp=int(input("Enter the experience: "))
rating=input("Enter performance rating(A/B/C): ")

bonus=0

if exp > 5:
    bonus = salary * 0.20
    
if rating == "A":
    bonus = bonus + (salary * 0.10)
    
elif rating == "B":
    bonus = bonus + (salary * 0.06)
    
total_salary = salary + bonus

print("Bonus : ",bonus)
print("Total salary: ",total_salary)