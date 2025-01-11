def describe_pet(animal_type,pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
    
describe_pet('hamster','harry')
describe_pet('Dog','bingo')

def describe_newpet(pet_name,animal_type="dog"):
    print(f"\n{pet_name}")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
    
describe_newpet(pet_name="willie")
describe_newpet('lucky')
describe_newpet(pet_name='kinsky',animal_type='cat')

