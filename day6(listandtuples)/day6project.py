
numbers = input("Enter numbers separated by spaces: ").split()

# Convert strings to numbers and calculate
numbers = [float(num) for num in numbers]
total = sum(numbers)
average = total / len(numbers)

print(f"Sum: {total}")
print(f"Average: {average}")