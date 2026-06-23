lunch =int(input("Enter lunch"))

match lunch:
    case 1:
        food=int(input("Enter food: "))
        
        match food:
            case 1:
                print("Pizza")
                
            case 2:
                print("Burger")
                
            case 3:
                print("Combo")
                
            case _:
                print("No Food")
                
    case 2:
        drink = int(input("Enter Drink: "))
        
        match drink:
            case 1:
                print("Tea")
                
            case 2:
                print("Coffee")
                
            case _:
                print("No Drinls...")
                
    case _:
        print("Invalid")
                
        
            