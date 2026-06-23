# Syntax:
    
#     match variable:
#     case value1:
#         # code
#     case value2:
#         # code
#     case _:
#         # default code


choice = 1

match choice:
    case 1:
        print("Start Game")
    case 2:
        print("Settings")
    case 3:
        print("Exit")
        
        
choice = int(input("Enter choice: "))

match choice:
    case 1:
        print("Addition")
        
    case 2:
        print("Subtraction")
        
    case 3:
        print("Multiplication")
        
    case 4:
        print("Division")
        
        
# default : case_

day = int(input("Enter day: "))

match day:
    case 1:
        print("Monday")
    
    case 2:
        print("Tuesday")
        
    case 3:
        print("Wednesday")
        
    case _:
        print("Invalid Day")
        