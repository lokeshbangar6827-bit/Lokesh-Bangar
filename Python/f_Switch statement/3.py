grade =(input("Enter Grade: "))

match grade:
    case 'A':
        print("Excellent")
        
    case 'B':
        print("Good")
        
    case 'C':
        print("Average")
        
    case 'D':
        print("Pass")
        
    case _:
        print("Fail")