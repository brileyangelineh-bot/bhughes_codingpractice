# List Statistics Tool

# Ask user for numbers
numbers_input = input("Enter numbers separated by spaces: ")

# Convert input string to a list of integers
numbers = [int(num) for num in numbers_input.split()]

# Calculate statistics
smallest = min(numbers)
largest = max(numbers)
total = sum(numbers)
average = total / len(numbers)

# Display results
print("Smallest number:", smallest)
print("Largest number:", largest)
print("Sum:", total)
print("Average:", round(average, 2))
