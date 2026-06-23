balance=int(input("Enter amount balance: "))
withdraw=int(input("Enter withdraw amount: "))

if withdraw % 100 != 0:
    print("Failure! Amount should be multiple of 100.")
elif balance <1000:
    print("Failure! Minimum balance of 1000 must remain.")
else:
    balance = balance - withdraw
    print("Balance =",balance)
