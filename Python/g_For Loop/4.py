print("-------------------HCF and LCM-------------------------------")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

hcf = 1

for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        hcf = i

lcm = (a * b) // hcf

print("HCF =", hcf)
print("LCM =", lcm)


print("----------------------------------------------------------------------")

total = 0

for i in range(1, 6):
    marks = int(input("Enter marks: "))
    total += marks

percent = (total / 500) * 100

if percent >= 90:
    grade = "A+"

elif percent >= 80:
    grade = "A"

elif percent >= 70:
    grade = "B"

elif percent >= 60:
    grade = "C"

elif percent >= 40:
    grade = "D"

else:
    grade = "Fail"

print("Total =", total)
print("Percentage =", percent)
print("Grade =", grade)


print("-----------------------------------------------------------")

n = int(input("Enter number of employees: "))

for i in range(1, n + 1):

    salary = float(input("Enter salary: "))

    if salary >= 50000:
        bonus = salary * 0.10
        tax = salary * 0.08

    elif salary >= 30000:
        bonus = salary * 0.05
        tax = salary * 0.05

    else:
        bonus = salary * 0.02
        tax = salary * 0.02

    final_salary = salary + bonus - tax

    print("Bonus =", bonus)
    print("Tax =", tax)
    print("Final Salary =", final_salary)
    
    print("-----------------------------------------------------------------")
    
    