# Asks a [question] then checks if the input is a usable number
def num_check(question):
    # Error messages
    error_1 = "Please enter a number that is more that 0"
    error_2 = "Please enter a number"

    while True: 
        try:
            response = float(input(question)) # asks question and stores the converts the input into a float

            if response and response > 0:
                return response
            else:
                # If the number is not above 0
                print(error_1)

        except ValueError:
            # If the input is not a number
            print(error_2)

keep_going = ""
while keep_going == "":
    # (assume they put in valid data)
    width = num_check("Width: ")
    height = num_check("Height: ")

    # Calculate area & perimeter
    area = width * height
    perimeter = 2 * (width + height)

    # Output the area and perimeter
    print()
    print(f"Area: {area} square units")
    print(f"Perimeter: {perimeter} units")

    # enables looping
    keep_going = input("press enter to keep going or press any key to quit")
    print()

print("thank you for using this calculator! :D")