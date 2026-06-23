print("GEO CALCI")
print("1. Triangle")
print("2. Rectangle")
print("3. Circle")
print("4. Exit")

choice = int(input("Enter your choice: "))

match choice:

    # Triangle
    case 1:
        print("\nTriangle")
        print("1. Area")
        print("2. Perimeter")
        print("3. Exit")

        ip = int(input("Enter your choice: "))

        match ip:
            case 1:
                base = float(input("Enter base: "))
                height = float(input("Enter height: "))
                area = 0.5 * base * height
                print("Area of Triangle =", area)

            case 2:
                a = float(input("Enter side 1: "))
                b = float(input("Enter side 2: "))
                c = float(input("Enter side 3: "))
                perimeter = a + b + c
                print("Perimeter of Triangle =", perimeter)

            case 3:
                print("Exit")

            case _:
                print("Invalid Choice")

    # Rectangle
    case 2:
        print("\nRectangle")
        print("1. Area")
        print("2. Perimeter")
        print("3. Exit")

        ip = int(input("Enter your choice: "))

        match ip:
            case 1:
                length = float(input("Enter length: "))
                width = float(input("Enter width: "))
                area = length * width
                print("Area of Rectangle =", area)

            case 2:
                length = float(input("Enter length: "))
                width = float(input("Enter width: "))
                perimeter = 2 * (length + width)
                print("Perimeter of Rectangle =", perimeter)

            case 3:
                print("Exit")

            case _:
                print("Invalid Choice")

    # Circle
    case 3:
        print("\nCircle")
        print("1. Area")
        print("2. Circumference")
        print("3. Exit")

        ip = int(input("Enter your choice: "))

        match ip:
            case 1:
                r = float(input("Enter radius: "))
                area = 3.14 * r * r
                print("Area of Circle =", area)

            case 2:
                r = float(input("Enter radius: "))
                circumference = 2 * 3.14 * r
                print("Circumference of Circle =", circumference)

            case 3:
                print("Exit")

            case _:
                print("Invalid Choice")

    # Exit
    case 4:
        print("Thank You!")

    case _:
        print("Invalid Choice")