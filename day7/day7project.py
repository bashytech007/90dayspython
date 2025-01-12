# Dictionary to store user information
user_database = {}

def add_user():
    name = input("Enter name: ")
    while True:
        try:
            age = int(input("Enter age: "))
            break
        except ValueError:
            print("Please enter a valid number for age")
    
    user_database[name] = age
    print(f"User {name} added successfully!")

def get_user():
    name = input("Enter name to search: ")
    if name in user_database:
        print(f"Name: {name}, Age: {user_database[name]}")
    else:
        print("User not found!")

def main():
    while True:
        print("\n1. Add user")
        print("2. Find user")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            add_user()
        elif choice == '2':
            get_user()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()