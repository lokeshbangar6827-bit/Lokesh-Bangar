menu = ((1, "paneer", 400), (2, "chiken", 600), (3, "dessert", 200), (4, "noodles", 150))

orders = []  # to store ordered items

while True:
    print("---HOTEL MENU CARD---\n1.View menu\n2.Order\n3.Generate Bill\n4.Exit\n")
    choice = int(input("Enter your choice\n"))
    
    match choice:
        case 1:
            print("items are :\n----------\nitem id    name    price\n---------")
            for items in menu:
                print(f"{items[0]}    {items[1]}    {items[2]}")
            print("-" * 40)
            
        case 2:
            item_id = int(input("Enter item id to order: "))
            qty = int(input("Enter quantity: "))
            found = False
            for items in menu:
                if items[0] == item_id:
                    orders.append((items[1], items[2], qty))
                    print(f"Order placed successfully! {items[1]} x {qty}")
                    found = True
                    break
            if not found:
                print("Invalid item id!")
            print("-" * 40)
                     
        case 3:
            if not orders:
                print("No items ordered yet!")
            else:
                print("\n--- BILL ---")
                total = 0
                for item in orders:
                    name, price, qty = item
                    cost = price * qty
                    total += cost
                    print(f"{name} x {qty} = {cost}")
                print(f"Total Bill = {total}")
            print("-" * 40)
            
        case 4:
            print("Thank you! Visit Again!")
            break
            
        case _:
            print("Invalid choice")