def get_valid_number():
    """
    Prompts user for a number and validates the input.
    Returns the valid integer input.
    Handles various error cases with appropriate messages.
    """
    while True:
        try:
            user_input = input("Please enter a number: ")
            number = int(user_input)
            return number
        except ValueError:
            if user_input.replace(".", "", 1).isdigit():
                print("Error: Please enter a whole number, not a decimal.")
            elif user_input.strip() == "":
                print("Error: Input cannot be empty. Please enter a number.")
            else:
                print(f"Error: '{user_input}' is not a valid number. Please enter a whole number.")
        except KeyboardInterrupt:
            print("\nProgram terminated by user.")
            exit()

def main():
    print("Welcome to the number validator!")
    number = get_valid_number()
    print(f"You successfully entered the number: {number}")

if __name__ == "__main__":
    main()