#Debugging Exercise 3: Function Not Behaving as Expected

'''Error to Expect: TypeError
 Hint: This code attempts to calculate the average of a list of numbers. However, one of the
 elements in the list is not a number in the conventional sense. How does Python treat
 different data types when performing arithmetic operations? Consider how you can ensure
 all elements are appropriately handled for the calculation.'''


def find_average(numbers):
    # Initialize variables
    sum = 0
    count_numbers = 0
    
    # Iterate through the elements in the list
    for number in numbers:
        # Attempt to add the number to the sum
        try:
            # Add the number to the sum
            sum += number
            # Increment the count of valid numbers
            count_numbers += 1
        except (TypeError, ValueError):
            # Print a warning if the element is not a valid number
            print(f"Warning: {number} is not a valid number and will be excluded from the average calculation.")
    
    # Check if there are valid numbers in the list
    if count_numbers == 0:
        print("Error: No valid numbers in the list.")
        return None
    
    # Calculate the average
    average = sum / count_numbers
    return average

# Example usage
numbers = [1, 2, 3, 4, 5, "not a number", 6]
average = find_average(numbers)

if average is not None:
    print(f"The average is: {average}")