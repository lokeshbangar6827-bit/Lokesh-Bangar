brand = int(input("Enter brand: "))

match brand:
    case 1:
        model = int(input("Enter model: "))

        match model:
            case 1:
                print("BMW X1")
            case 2:
                print("BMW X5")
            case _:
                print("Invalid Model")

    case 2:
        model = int(input("Enter model: "))

        match model:
            case 1:
                print("Audi A4")
            case 2:
                print("Audi Q7")
            case _:
                print("Invalid Model")

    case _:
        print("Invalid Brand")