#project day 3
def check_age_eligibility():
    try:
        # Get age input from user
        age = int(input("Please enter your age: "))
        
        # Check for valid age
        if age < 0 or age > 120:
            print("Please enter a valid age between 0 and 120.")
            return False
            
        # Check various age-based eligibilities
        if age >= 18:
            print("You are eligible to:")
            print("- Vote")
            print("- Get a driver's license")
            print("- Work full-time")
        else:
            remaining_years = 18 - age
            print(f"You are too young for adult services. You need to wait {remaining_years} more years.")
            
        # Additional age-specific checks
        if age >= 21:
            print("- Purchase and consume alcohol (in the US)")
            
        if age >= 25:
            print("- Rent a car without additional fees (in most places)")
            
        if age >= 65:
            print("- Qualify for senior citizen benefits")
            
        # Special message for young children
        if age < 13:
            print("\nYou can still enjoy:")
            print("- Watch age-appropriate movies")
            print("- Participate in youth sports")
            print("- Join school clubs")
            
        return True
            
    except ValueError:
        print("Please enter a valid number for age.")
        return False

print("Welcome to the Age Eligibility Checker!")
check_age_eligibility()